# Generated by Django 2.2.16 on 2022-11-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='mailing',
            options={'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='code',
            field=models.PositiveIntegerField(verbose_name='Код телефона'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.PositiveIntegerField(unique=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tag',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Тэг'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='time_zone',
            field=models.CharField(max_length=10, verbose_name='Часовой пояс'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='code',
            field=models.CharField(max_length=50, verbose_name='Коды телефона'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='end_send_time',
            field=models.DateTimeField(verbose_name='Время завершения рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start_send_time',
            field=models.DateTimeField(verbose_name='Время начала рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='tag',
            field=models.CharField(max_length=150, verbose_name='Тэги'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='text',
            field=models.TextField(verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='message',
            name='send_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки'),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('SEND', 'message has been sent'), ('FAILED', 'message failed'), ('PROCESSED', 'message is being processed')], max_length=10, verbose_name='Статус отправки'),
        ),
    ]