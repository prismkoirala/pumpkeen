from django import forms

OIL_CHOICES = (
    ("1", "Diesel"),
    ("2", "Petrol")
)

class BillingForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    oil = forms.ChoiceField(choices = OIL_CHOICES)
    amount = forms.IntegerField()

  