from django.shortcuts import render
from .models import *
import secrets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from datetime import datetime, timedelta, date
from encodedecode import encode, decode
from django.conf import settings
from django.core.mail import send_mail

present_time = datetime.now()

'{:%H:%M:%S}'.format(present_time)
updated_time = datetime.now() + timedelta(hours=20)


def check_auth(Authkey):
    present_time = datetime.now()
    '{:%H:%M:%S}'.format(present_time)
    updated_time = datetime.now()
    if Tokens.objects.filter(Auth=Authkey):
        Auth = Tokens.objects.get(Auth=Authkey)
        serializer = TokensSerializer(Auth, many=False)
        expire_time = serializer.data.get('expires')
        expire_time = expire_time.replace('Z', "")
        expire_time = datetime.strptime(expire_time, '%Y-%m-%dT%H:%M:%S.%f')
        if updated_time > expire_time:
            return False
        else:
            return True


@api_view(['POST'])
def loginuser(request):
    username = request.data.get('email')
    password = request.data.get('password')
    if Accounts.objects.filter(email=username).exists() and Accounts.objects.filter(password=encode(password)):
        response_data = {
            'authKey': setAuth(username),
            'time_expire': updated_time,
            'user': username
        }
        return Response(response_data)
    else:
        return Response("Not Logged...")


def setAuth(username):
    authKey = secrets.token_hex(20)
    value = {'Auth': authKey, 'expires': updated_time, 'user': username}
    expire_time = updated_time
    serializer = TokensSerializer(data=value)
    if serializer.is_valid():
        serializer.save()
    else:
        return JsonResponse(value, safe=False)
    return authKey


@api_view(['POST'])
def createUser(request):
    name = request.data.get('user')
    company = request.data.get('shop_name')
    email = request.data.get('email')
    password = request.data.get('password')
    hash_password = encode(password)
    data = {'user': name, 'shop_name': company,
            'email': email, 'password': hash_password}
    serializer = AccountsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        # subject = 'Shop Created Successfully'
        # message = f'Hi {name}, thank you for Using in {company}.'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [request.data.get('email'), ]
        # try:
        #     send_mail(subject, message, email_from, recipient_list)
        # except BaseException as e:
        #     return Response(e)
    else:
        print(request.data, "invalid data got")

    return Response(serializer.data)
