from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'


class TotalBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalBill
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class TotalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTotal
        fields = '__all__'


class CashInHandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashInHand
        fields = '__all__'
