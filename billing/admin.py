from django.contrib import admin
from .models import OilType, Billing, BillingHistory

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

@admin.register(BillingHistory)
class BillingAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'oil',
        'quantity',
        'amount'
    ]
    list_display =[
        'name',
        'oil',
        'quantity',
        'amount'
    ]
    list_filter =[
        'name'
    ]
    search_fields = ['oil']

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
