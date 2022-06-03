from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from .models import TransactionHistory
from .forms import RegularTradeForm

def index(request):
    return render(request, 'index.html', {})

def transaction_history(request):
    transaction_history_data = TransactionHistory.objects.all().order_by('-id') 
    return render(request, 'transaction_history.html', {'history': transaction_history_data})

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

def trade_calculator(request):
    return render(request, 'trade_calculator.html', {})

def settings(request):
    return render(request, 'settings.html', {})


def delete_transaction_history(request, pk):
    transation = get_object_or_404(TransactionHistory, pk=pk)
    transation.delete()

    return redirect('transaction_history')