from django.contrib import admin
from .models import Category, Laptop, Phone, Accessory, OfferedProduct


admin.site.register(Category)
admin.site.register(Laptop)
admin.site.register(Phone)
admin.site.register(Accessory)
admin.site.register(OfferedProduct)
