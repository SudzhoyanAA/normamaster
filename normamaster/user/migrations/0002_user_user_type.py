# Generated by Django 3.2.3 on 2024-04-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('client', 'Клиент'), ('specialist', 'Специалист')], default='client', max_length=20, verbose_name='Тип пользователя'),
        ),
    ]
