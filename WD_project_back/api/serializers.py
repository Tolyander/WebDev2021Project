from rest_framework import serializers
from api.models import *


class LaptopSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    rating = serializers.FloatField()
    url = serializers.CharField()
    image = serializers.CharField()
    category = serializers.CharField(read_only=True)


class PhoneSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    rating = serializers.FloatField()
    url = serializers.CharField()
    image = serializers.CharField()
    category = serializers.CharField(read_only=True)


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = ('id', 'name', 'price', 'description', 'rating', 'url', 'category', 'image')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferedProduct
        fields = ('id', 'name', 'price', 'company')
