from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Billing, BillingHistory, OilType
from .forms import BillingForm

def billing(request, *args, **kwargs):

    oil = OilType.objects.all()
    billings = Billing.objects.all()
    history = BillingHistory.objects.all().order_by('-id')[:5]
    form = BillingForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():

            form_name = form.cleaned_data.get('name')
            form_amt = form.cleaned_data.get('amount')



            oil_id = form.cleaned_data.get('oil')
            oil_obj = OilType.objects.get(id=oil_id)

            curr_price = oil_obj.price
            quantity =  form_amt/oil_obj.price

            history_save = BillingHistory(
                oil = oil_obj,
                price = curr_price,
                name = form_name,
                quantity = quantity,
                amount = form_amt
            )
            history_save.save()

            post_obj = BillingHistory.objects.all().last()

            return render(request, 'post.html', {'obj': post_obj})
    else:
        pass

    context = {
        'billings' : billings,
        'history' : history,
        'form': form,
        'oil': oil
     }

    return render(request, 'home.html', context)

def list_billing(request, *args, **kwargs):

    history = BillingHistory.objects.all().order_by('-id')   

    context = {
        'history' : history,
     }

    return render(request, 'billing_history.html', context)


def printing_page(request, *args, **kwargs):

    return render(request, 'post.html')