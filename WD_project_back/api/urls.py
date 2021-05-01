from django.urls import path
from api.views import *
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token),

    path('products/', product_list),

    path('products/laptop/', LaptopListAPIView.as_view()),
    path('products/laptop/<int:pk>/', LaptopDetailAPIView.as_view()),

    path('products/phone/', PhoneListAPIView.as_view()),
    path('products/phone/<int:pk>/', PhoneDetailAPIView.as_view()),

    # for fbv
    # path('products/accessory/', accessory_list),
    # path('products/accessory/<int:accessory_id>/', accessory_item),

    # path('products/offer/', offered_product_list),
    # path('products/offer/<int:offer_id>/', offered_product_item)

    # for generic views
    path('products/accessory/', AccessoryListAPIView.as_view()),
    path('products/accessory/<int:pk>/', AccessoryDetailAPIView.as_view()),

    path('products/offer/', OfferListAPIView.as_view()),
    path('products/offer/<int:pk>/', OfferDetailAPIView.as_view()),
]