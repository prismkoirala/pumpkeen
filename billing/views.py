from django.shortcuts import render
from .models import Billing

def list_billing(request, *args, **kwargs):
    billings = Billing.objects.all()
    context = { 'billings' : billings }
    return render(request, 'home.html', context)

# Create your views here.
