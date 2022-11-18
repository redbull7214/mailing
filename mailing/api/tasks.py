import os
import requests
import pytz
import datetime
from dotenv import load_dotenv
from celery.utils.log import get_task_logger

from .models import Message, Client, Mailing
from mailing.celery import app

logger = get_task_logger(__name__)

load_dotenv()
URL = 'https://probe.fbrq.cloud/v1/send/'
TOKEN = os.getenv("TOKEN")


@app.task(bind=True, retry_backoff=True)
def send_message(self, data, client_id, mailing_id, url=URL, token=TOKEN):

    mail = Mailing.objects.get(pk=mailing_id)
    client = Client.objects.get(pk=client_id)
    timezone = pytz.timezone(client.timezone)
    now = datetime.datetime.now(timezone)

    if mail.start_send_time <= now.time() <= mail.end_send_time:
        header = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}
        try:
            requests.post(url=url + str(data['id']), headers=header, json=data)
        except requests.exceptions.RequestException as exc:
            logger.error(f"Message if: {data['id']} is error")
            Message.objects.filter(pk=data['id']).update(status='FAILED')
            raise self.retry(exc=exc)
        else:
            logger.info(f"Message id: {data['id']}, Sending status: 'Sent'")
            Message.objects.filter(pk=data['id']).update(status='SEND')
    else:
        time = 24 - (int(now.time().strftime('%H:%M:%S')[:2]) -
                     int(mail.start_send_time.strftime('%H:%M:%S')[:2]))
        logger.info(f"Message id: {data['id']}, "
                    f"The current time is not for sending the message,"
                    f"restarting task after {60*60*time} seconds")
        return self.retry(countdown=60*60*time)
