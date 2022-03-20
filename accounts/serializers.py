from rest_framework import serializers
from .models import Accounts, Tokens


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'


class TokensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokens
        fields = '__all__'
