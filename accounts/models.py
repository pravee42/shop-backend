from django.db import models
from datetime import datetime, timedelta, date

# Create your models here.


class Accounts(models.Model):
    shop_name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.shop_name


class Tokens(models.Model):
    Auth = models.CharField(max_length=200, default="")
    expires = models.DateTimeField(default=datetime.now)
    user = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.user
