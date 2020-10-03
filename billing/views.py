from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Billing, BillingHistory, OilType
from .forms import BillingForm

def list_billing(request, *args, **kwargs):

    billings = Billing.objects.all()
    history = BillingHistory.objects.all()
    form = BillingForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form_name = form.cleaned_data.get('name')

            oil_name = 'Petrol'
            oil_obj = OilType.objects.get(name=oil_name)

            history_save = BillingHistory(
                oil = oil_obj,
                name = form_name,
                quantity = 5,
                total = 1000
            )
            history_save.save()
            return render(request, 'post.html')
    else:
        pass

    context = {
        'billings' : billings,
        'history' : history,
        'form': form
     }

    return render(request, 'home.html', context)

# Create your views here.
