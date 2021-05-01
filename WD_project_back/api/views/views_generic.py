from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from api.serializers import *
from api.models import *
import json


class LaptopListAPIView(generics.ListCreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    permission_classes = (IsAuthenticated,)


class LaptopDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    permission_classes = (IsAuthenticated,)


class PhoneListAPIView(generics.ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = (IsAuthenticated,)


class PhoneDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = (IsAuthenticated,)


class AccessoryListAPIView(generics.ListCreateAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = (IsAuthenticated,)


class AccessoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = (IsAuthenticated,)


class OfferListAPIView(generics.ListCreateAPIView):
    queryset = OfferedProduct.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (IsAuthenticated,)


class OfferDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfferedProduct.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (IsAuthenticated,)
