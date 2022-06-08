import requests
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from .models import TransactionHistory, TickerData
from .forms import RegularTradeForm, TickerForm
from .filters import TransactionHistoryFilter

############ PAGES URL ############

def index(request):
    return render(request, 'index.html', {})

def transaction_history(request):
    transaction_history_data = TransactionHistory.objects.all()

    historyFilter = TransactionHistoryFilter(request.GET, queryset=transaction_history_data)
    transaction_history_data = historyFilter.qs

    context = {
        'history': transaction_history_data,
        'historyFilter': historyFilter,
    }

    return render(request, 'transaction_history.html', context)

def trade_regular_trade(request):
    form = RegularTradeForm()
    if request.method == 'POST':
        form = RegularTradeForm(request.POST)
        if form.is_valid():
            buy_currency = request.POST['buy_currency']
            buy_currency_amount = request.POST['buy_currency_amount']
            sell_currency = request.POST['sell_currency']
            sell_currency_amount = request.POST['sell_currency_amount']

            complete_order = TransactionHistory(
                buy_currency = buy_currency,
                buy_currency_amount = buy_currency_amount,
                sell_currency = sell_currency,
                sell_currency_amount = sell_currency_amount
            )
            complete_order.save()
            messages.success(request, ('Transaction completed successfully'))
            
            return redirect('transaction_history')
        else:
            messages.success(request, (form.errors))
    
        return redirect('trade_regular_trade')
    return render(request, 'trade_regular_trade.html', {'form': form})

def settings(request):
    ticker_form = TickerForm()
    ticker_currency_arr = TickerData.objects.all()

    context = {
        'ticker_form': ticker_form,
        'ticker_currency_arr': ticker_currency_arr
    }

    return render(request, 'settings.html', context)

############ BACKEND URL ############

# backend-validation
def update_ticker_data(request):
    currency = request.POST['currency']

    if TickerData.objects.filter(currency=currency).exists():
        messages.success(request, ('Current currency already in list'))
    else:
        ticker_currency = TickerData(currency=currency)
        ticker_currency.save()
    
    return redirect('settings')

def delete_ticker_data(request, pk):
    ticker_currency = get_object_or_404(TickerData, pk=pk)
    ticker_currency.delete()

    return redirect('settings')

def delete_transaction_history(request, pk):
    transation = get_object_or_404(TransactionHistory, pk=pk)
    transation.delete()

    return redirect('transaction_history')
