
from django import forms
from.models import stationdetails

class mapitem(forms.ModelForm):
    class Meta:
        model = stationdetails
        fields = ['name', 'latitude', 'longitude']


class PaymentForm(forms.Form):
    amount_display = forms.DecimalField(decimal_places=2, disabled=True, label="Amount",required=False)
    amount = forms.DecimalField(decimal_places=2, widget=forms.HiddenInput())
    currency = forms.CharField(max_length=3, initial='usd')