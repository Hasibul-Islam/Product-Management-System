from django.contrib import admin

# Register your models here.

from .models import ProductType, Order, Costing, YearlyProfit


admin.site.register(Order)
admin.site.register(ProductType)
admin.site.register(Costing)
admin.site.register(YearlyProfit)