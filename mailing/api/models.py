from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):

    number = models.PositiveIntegerField(
        validators=[
            RegexValidator(r'^((7)+([0-9]){10})$',
                           message='Введите номер в формате 7XXXXXXXXXX')
        ],
        unique=True,
        verbose_name='Номер телефона',
    )
    code = models.PositiveIntegerField(
        validators=[
            RegexValidator(r'^[0-9]{3}$',
                           message='Введите код в формате XXX')
        ],
        verbose_name='Код телефона',
    )
    tag = models.CharField(null=True, blank=True,
                           max_length=50, verbose_name='Тэг',)
    time_zone = models.CharField(max_length=10, verbose_name='Часовой пояс')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Mailing(models.Model):
    start_send_time = models.DateTimeField(
        verbose_name='Время начала рассылки')
    text = models.TextField(verbose_name='Комментарий')
    tag = models.CharField(max_length=150, verbose_name='Тэги')
    code = models.CharField(max_length=50, verbose_name='Коды телефона')
    end_send_time = models.DateTimeField(
        verbose_name='Время завершения рассылки')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    STATUS_CHOICES = (
        ('SEND', 'message has been sent'),
        ('FAILED', 'message failed'),
        ('PROCESSED', 'message is being processed')
    )
    send_time = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата отправки')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, verbose_name='Статус отправки')
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
