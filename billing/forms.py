from django import forms
from .models import OilType

OIL_CHOICES = (
    ("1", "Diesel"),
    ("2", "Petrol")
)
NAME_CHOICES = (
    ("Shyam", "Shyam Magar"),
    ("Devi", "Devi Koirala")
)

class DieselUpdateForm(forms.Form):
	price = forms.DecimalField()
	price.widget.attrs.update({'class': "input is-large"})

class OilUpdateForm(forms.ModelForm):
	
    class Meta:
        model = OilType
        fields = ['price']
	
class BillingForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': "input is-large"}))
    oil = forms.ChoiceField(choices = OIL_CHOICES,widget=forms.Select(attrs={'class': "control select is-large"}))
    amount = forms.IntegerField()
    amount.widget.attrs.update({'class': "input is-large"})