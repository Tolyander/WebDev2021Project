from rest_framework.decorators import api_view

from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models import *
from api.serializers import *
import json


@api_view(['GET'])
def product_list(request):
    products_json = []
    products1 = Laptop.objects.all()
    for product in products1:
        products_json.append(product.to_json())

    products2 = Phone.objects.all()
    for product in products2:
        products_json.append(product.to_json())

    products3 = Accessory.objects.all()
    for product in products3:
        products_json.append(product.to_json())
    return Response(products_json)


@api_view(['GET'])
def laptop_list(request):
    laptops = Laptop.objects.all()
    serializer = LaptopSerializer(laptops, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def laptop_item(request, laptop_id):
    try:
        laptops = Laptop.objects.get(id=laptop_id)
    except Laptop.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)
    return Response(laptops.to_json())


@api_view(['GET'])
def phone_list(request):
    phones = Phone.objects.all()
    serializer = PhoneSerializer(phones, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def phone_item(request, phone_id):
    try:
        phones = Phone.objects.get(id=phone_id)
    except Phone.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)
    return Response(phones.to_json())


@api_view(['GET', 'POST'])
def accessory_list(request):
    if request.method == 'GET':
        accessories = Accessory.objects.all()
        serializer = AccessorySerializer(accessories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = AccessorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET'])
def accessory_item(request, accessory_id):
    try:
        accessories = Accessory.objects.get(id=accessory_id)
    except Accessory.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return Response(accessories.to_json())


@api_view(['GET', 'POST'])
def offered_product_list(request):
    if request.method == 'GET':
        offers = OfferedProduct.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            offer = OfferedProduct.objects.create(name=data['name'], price=data['price'], company=data['company'])
        except Exception as e:
            return Response({'message': str(e)})

        return Response(offer.to_json())


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def offered_product_item(request, offer_id):
    try:
        offers = OfferedProduct.objects.get(id=offer_id)
    except OfferedProduct.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        return Response(offers.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        offers.name = data['name']
        offers.save()
        return Response(offers.to_json())
    elif request.method == 'DELETE':
        offers.delete()
        return Response({"message": "product deleted"})
