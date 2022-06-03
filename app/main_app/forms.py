from locale import currency
from django import forms
from .models import TransactionHistory

class RegularTradeForm(forms.Form):
    buy_currency = forms.CharField(
        max_length=50,
        label='Buy currency',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    buy_currency_amount = forms.FloatField(
        label='Buy currency amount',
        widget=forms.NumberInput(attrs={
            'class': 'form-control'
        })
    )

    sell_currency = forms.CharField(
        max_length=50,
        label='Sell currency',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    sell_currency_amount = forms.FloatField(
        label='Sell currency amount',
        widget=forms.NumberInput(attrs={
            'class': 'form-control'
        })
    )