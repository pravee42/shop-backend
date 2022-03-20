from django.db import models
from datetime import datetime, timedelta, date

# Create your models here.


class Products(models.Model):
    shop_email = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_qty = models.IntegerField()
    product_gst = models.FloatField()
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return self.shop_email


class Bill(models.Model):
    shop_email = models.CharField(max_length=200)
    bill_number = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    product_id = models.IntegerField(default=0)
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_qty = models.IntegerField()
    product_gst = models.FloatField()
    total_price = models.IntegerField()

    def __int__(self):
        return self.bill_number


class TotalBill(models.Model):
    shop_email = models.CharField(max_length=200)
    bill_number = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    total_ammount = models.IntegerField()

    def __int__(self):
        return self.bill_number


class Service(models.Model):
    shop_email = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    service_number = models.IntegerField()
    service_name = models.CharField(max_length=200)
    price = models.IntegerField()
    product_gst = models.FloatField()
    total_price = models.IntegerField()

    def __int__(self):
        return self.service_number


class ServiceTotal(models.Model):
    shop_email = models.CharField(max_length=200)
    service_number = models.IntegerField()
    date = models.CharField(max_length=200)
    total_price = models.IntegerField()

    def __int__(self):
        return self.service_number


class CashInHand(models.Model):
    shop_email = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    ammount = models.IntegerField()

    def __str__(self):
        return self.shop_email
