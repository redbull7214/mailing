import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailing.settings')

app = Celery(
    'backend',
    broker=os.getenv('BROKER', default='redis://redis')
)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_url = os.getenv('BROKER_URL', default='redis://redis:6379/0')

app.conf.timezone = 'Europe/Moscow'

app.autodiscover_tasks()
