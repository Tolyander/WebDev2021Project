from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from api.models import Laptop, Phone, Accessory, OfferedProduct
from django.views.decorators.csrf import csrf_exempt
import json
from api.serializers import *
from rest_framework.response import Response
from rest_framework.request import Request


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
    return JsonResponse(products_json, safe=False)


def laptop_list(request):
    laptops = Laptop.objects.all()
    serializer = LaptopSerializer(laptops, many=True)
    return JsonResponse(serializer.data, safe=False)


def laptop_item(request, laptop_id):
    try:
        laptops = Laptop.objects.get(id=laptop_id)
    except Laptop.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(laptops.to_json())


def phone_list(request):
    phones = Phone.objects.all()
    serializer = PhoneSerializer(phones, many=True)
    return JsonResponse(serializer.data, safe=False)


def phone_item(request, phone_id):
    try:
        phones = Phone.objects.get(id=phone_id)
    except Phone.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(phones.to_json())


def accessory_list(request):
    if request.method == 'GET':
        accessories = Accessory.objects.all()
        serializer = AccessorySerializer(accessories, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = AccessorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


def accessory_item(request, accessory_id):
    try:
        accessories = Accessory.objects.get(id=accessory_id)
    except Accessory.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(accessories.to_json())


@csrf_exempt
def offered_product_list(request):
    if request.method == 'GET':
        offers = OfferedProduct.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            offer = OfferedProduct.objects.create(name=data['name'], price=data['price'], company=data['company'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(offer.to_json())


@csrf_exempt
def offered_product_item(request, offer_id):
    try:
        offers = OfferedProduct.objects.get(id=offer_id)
    except OfferedProduct.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(offers.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        offers.name = data['name']
        offers.save()
        return JsonResponse(offers.to_json())
    elif request.method == 'DELETE':
        offers.delete()
        return JsonResponse({"message": "product deleted"})



