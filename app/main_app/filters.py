from django import forms
import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter

from .models import TransactionHistory
from .widgets import DatePickerInput

class TransactionHistoryFilter(django_filters.FilterSet):
    buy_currency = CharFilter(
        field_name='buy_currency', 
        lookup_expr='iexact', 
        label='Bought currency',
        widget=forms.TextInput(attrs={'class': 'form-control currency-autocomplete'})
    )
    buy_currency_amount_from = NumberFilter(
        field_name='buy_currency_amount', 
        lookup_expr='gt', 
        label='Amount',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'From'})
    )
    buy_currency_amount_to = NumberFilter(
        field_name='buy_currency_amount', 
        lookup_expr='lt', 
        label='Amount',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'To'})
    )
    sell_currency = CharFilter(
        field_name='sell_currency', 
        lookup_expr='iexact', 
        label='Sold currency',
        widget=forms.TextInput(attrs={'class': 'form-control currency-autocomplete'})
    )
    sell_currency_amount_from = NumberFilter(
        field_name='sell_currency_amount', 
        lookup_expr='gt', 
        label='Amount',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'From'})
    )
    sell_currency_amount_to = NumberFilter(
        field_name='sell_currency_amount', 
        lookup_expr='lt', 
        label='Amount',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'To'})
    )
    start_date = DateFilter(
        field_name='date', 
        lookup_expr='gte', 
        label='Date',
        widget=DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'From'})
    )
    end_date = DateFilter(
        field_name='date', 
        lookup_expr='lte', 
        label='Date',
        widget=DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'To'})
    )

    class Meta:
        model = TransactionHistory
        fields = ''