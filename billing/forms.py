from django import forms

OIL_CHOICES = (
    ("1", "Diesel"),
    ("2", "Petrol")
)

class BillingForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': "input is-large"}))
    oil = forms.ChoiceField(choices = OIL_CHOICES,widget=forms.Select(attrs={'class': "control select is-large"}))
    amount = forms.IntegerField()
    amount.widget.attrs.update({'class': "input is-large"})