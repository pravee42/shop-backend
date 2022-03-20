from django.shortcuts import render
from .models import *
from accounts.models import Tokens
from accounts.serializers import TokensSerializer
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status


def Auth(token):
    if Tokens.objects.filter(Auth=token).exists():
        return True
    else:
        return False


def AuthEmail(token):
    data = Tokens.objects.get(Auth=token)
    serializer = TokensSerializer(data, many=False)
    return serializer.data.get('user')


class ProductView(APIView):

    def get(self, request, pk, format=None):
        if Auth(pk) == True:
            email = AuthEmail(pk)
            data = Products.objects.filter(shop_email=email)
            serializer = ProductsSerializer(data, many=True)
            return Response(serializer.data)
        return Response("Not Logged in", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk, format=None):
        if Auth(pk) == True:
            serializer = ProductsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Not Logged in", status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(id=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            serializer = ProductsSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Not Logged in", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            serializer = ProductsSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)


class BillView(APIView):
    def get(self, request, pk, format=None):
        if Auth(pk) == True:
            data = Bill.objects.filter(shop_email=AuthEmail(pk))
            serializer = BillSerializer(data, many=True)
            return Response(serializer.data)
        else:
            return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk, format=None):
        if Auth(pk) == True:
            serializer = BillSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)


class BillDetailView(APIView):
    def get_object(self, pk):
        try:
            return Bill.objects.get(id=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            serializer = BillSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Not Logged in", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            serializer = BillSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)


class ServiceView(APIView):
    def get(self, request, pk, format=None):
        if Auth(pk) == True:
            data = Service.objects.filter(shop_email=AuthEmail(pk))
            serializer = ServiceSerializer(data, many=True)
            return Response(serializer.data)
        else:
            return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk, format=None):
        if Auth(pk) == True:
            serializer = ServiceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)


class ServiceDetailView(APIView):
    def get_object(self, pk):
        try:
            return Service.objects.get(id=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            serializer = ServiceSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Not Logged in", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            serializer = ServiceSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)


class TotalBillView(APIView):
    def get(self, request, pk, format=None):
        if Auth(pk) == True:
            data = TotalBill.objects.filter(shop_email=AuthEmail(pk))
            serializer = TotalBillSerializer(data, many=True)
            return Response(serializer.data)
        else:
            return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk, format=None):
        if Auth(pk) == True:
            serializer = TotalBillSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)


class TotalBillDetailView(APIView):
    def get_object(self, pk):
        try:
            return TotalBill.objects.get(id=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            serializer = TotalBillSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Not Logged in", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            serializer = TotalBillSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)


class TotalServiceView(APIView):
    def get(self, request, pk, format=None):
        if Auth(pk) == True:
            data = ServiceTotal.objects.filter(shop_email=AuthEmail(pk))
            serializer = TotalServiceSerializer(data, many=True)
            return Response(serializer.data)
        else:
            return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk, format=None):
        if Auth(pk) == True:
            serializer = TotalServiceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)


class TotalServiceDetailView(APIView):
    def get_object(self, pk):
        try:
            return ServiceTotal.objects.get(id=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            serializer = TotalServiceSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Not Logged in", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            serializer = TotalServiceSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)


class CashinHandView(APIView):
    def get(self, request, pk, format=None):
        if Auth(pk) == True:
            data = CashInHand.objects.filter(shop_email=AuthEmail(pk))
            serializer = CashInHandSerializer(data, many=True)
            return Response(serializer.data)
        else:
            return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk, format=None):
        if Auth(pk) == True:
            serializer = CashInHandSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)


class CashinHandDetailView(APIView):
    def get_object(self, pk):
        try:
            return CashInHand.objects.get(id=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            serializer = CashInHandSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Not Logged in", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            serializer = CashInHandSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tk, pk, format=None):
        if Auth(tk) == True:
            data = self.get_object(pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("Auth Failed", status=status.HTTP_400_BAD_REQUEST)
