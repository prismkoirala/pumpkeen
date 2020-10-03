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
            form_amt = form.cleaned_data.get('amount')



            oil_id = form.cleaned_data.get('oil')
            oil_obj = OilType.objects.get(id=oil_id)

            quantity =  form_amt/oil_obj.price

            history_save = BillingHistory(
                oil = oil_obj,
                name = form_name,
                quantity = quantity,
                amount = form_amt
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

