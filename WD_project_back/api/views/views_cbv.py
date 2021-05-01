from django.shortcuts import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.serializers import *
from api.models import *
from rest_framework.permissions import IsAuthenticated


class LaptopListAPIView(APIView):
    def get(self, request):
        laptops = Laptop.objects.all()
        serializer = LaptopSerializer(laptops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LaptopDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Laptop.objects.get(id=pk)
        except Laptop.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        laptop = self.get_object(pk)
        serializer = LaptopSerializer(laptop)
        return Response(serializer.data)


class PhoneListAPIView(APIView):
    def get(self, request):
        phones = Phone.objects.all()
        serializer = PhoneSerializer(phones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PhoneDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Phone.objects.get(id=pk)
        except Phone.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        phone = self.get_object(pk)
        serializer = PhoneSerializer(phone)
        return Response(serializer.data)
