from django.contrib import admin
from .models import *
# Register your models here.
models = [Products, Bill, TotalBill,
          Service, ServiceTotal, CashInHand]

for x in models:
    admin.site.register(x)
