from django.contrib import admin
from .models import OilType, Billing

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'oil',
        'quantity',
    ]
    list_display =[
        'name',
        'oil',
        'quantity',

    ]
    list_filter =[
        'name'
    ]
    search_fields = ['oil']
# Register your models here.
@admin.register(OilType)
class OilAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'price'
    ]
    list_display =[
        'name',
        'price',

    ]
    list_filter =[
        'name'
    ]
    search_fields = ['name']
# Register your models here.
