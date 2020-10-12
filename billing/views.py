from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect

from .models import Billing, BillingHistory, OilType
from .forms import BillingForm, DieselUpdateForm, OilUpdateForm

def billing_exec(request, *args, **kwargs):

    oil = OilType.objects.all()
    billings = Billing.objects.all()
    history = BillingHistory.objects.all()[:5]
    form = BillingForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():

            form_name = form.cleaned_data.get('name')
            form_amt = form.cleaned_data.get('amount')

            oil_id = form.cleaned_data.get('oil')
            oil_obj = OilType.objects.get(id=oil_id)

            curr_price = oil_obj.price
            quantity =  form_amt/oil_obj.price

            prof = oil_obj.price-oil_obj.cp
            tot_prof = quantity

            history_save = BillingHistory(
                oil = oil_obj,
                price = curr_price,
                name = form_name,
                quantity = quantity,
                amount = form_amt,
            )
            history_save.save()

            post_obj = BillingHistory.objects.first()

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
    
    tot = 0
    prof = 4.5
    tot_prof=0.00

    for ins in history:

        tot = tot + ins.amount
        tot_prof = tot_prof+ins.profit

    paginator = Paginator(history, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'history' : history,
        'page_obj': page_obj,
        'tot': tot,
        'tot_prof':tot_prof
     }

    return render(request, 'billing/billing_history.html', context=context)


def printing_page(request, *args, **kwargs):

    return render(request, 'billing/post.html')

def settings_view(request, *args, **kwargs):

    oil = OilType.objects.all()

    context={
        'oil': oil
    }

    return render(request, 'config/settings.html', context)




def edit_oil(request, id):

    if request.method == "POST":
        form = OilUpdateForm(request.POST or None)

        if form.is_valid():

            oil_price = form.cleaned_data.get('price')
            oil = OilType.objects.filter(id=id).update(price=oil_price)  
            success = "Successfully configured!"
            return render(request, 'info.html', {'success':success})
    
    else:
        oil = OilType.objects.get(id=id)
        form = OilUpdateForm(request.POST)
        context={
            'oil': oil,
            'form': form
        }
        return render(request, 'config/edit_oil.html', context)