# Generated by Django 4.0.3 on 2022-03-14 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tokens',
            name='login_token',
        ),
        migrations.RemoveField(
            model_name='tokens',
            name='login_user',
        ),
        migrations.RemoveField(
            model_name='tokens',
            name='user_id',
        ),
        migrations.AddField(
            model_name='tokens',
            name='Auth',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tokens',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='tokens',
            name='user',
            field=models.CharField(default='', max_length=200),
        ),
    ]
