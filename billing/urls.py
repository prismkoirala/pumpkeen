from .views import billing_exec, list_billing
from django.urls import path

billing = path

urlpatterns = [
	path('', billing_exec, name="billing_exec" ),
	path('billings/', list_billing, name="list_billing" ),
]