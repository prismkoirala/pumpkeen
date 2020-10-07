from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Billing, BillingHistory, OilType
from .forms import BillingForm, DieselUpdateForm, PetrolUpdateForm

def billing_exec(request, *args, **kwargs):

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

            return render(request, 'billing/post.html', {'obj': post_obj})
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

    paginator = Paginator(history, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'history' : history,
        'page_obj': page_obj
     }

    return render(request, 'billing/billing_history.html', context=context)


def printing_page(request, *args, **kwargs):

    return render(request, 'billing/post.html')

def settings_view(request, *args, **kwargs):

    return render(request, 'config/settings.html')

def update_diesel(request, *args, **kwargs):

    diesel_update_form = DieselUpdateForm(request.POST or None)

    if request.method == 'POST':
        if diesel_update_form.is_valid():
            diesel_price = diesel_update_form.cleaned_data.get('price')

            update_diesel = OilType.objects.filter(id=1).update(price=diesel_price) 

            diesel_success = "Diesel has been succesfully Configured!"

            context={
            'success' : diesel_success
            }

            return render(request, 'info.html', context=context )

    else:
        pass

    context = {
        'diesel_update_form': diesel_update_form
    }

    return render(request, 'config/update_diesel.html', context)

def update_petrol(request, *args, **kwargs):

    petrol_update_form = PetrolUpdateForm(request.POST or None)

    if request.method == 'POST':
        if petrol_update_form.is_valid():
            petrol_price = petrol_update_form.cleaned_data.get('price')

            update_petrol = OilType.objects.filter(id=2).update(price=petrol_price) 

            petrol_success = "Petrol has been succesfully Configured!"

            context={
            'success' : petrol_success
            }

            return render(request, 'info.html', context=context )

    else:
        pass

    context = {
        'petrol_update_form': petrol_update_form
    }

    return render(request, 'config/update_petrol.html', context)