import requests
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import TransactionHistory, TickerData
from .forms import RegularTradeForm, TickerForm, CreateUserForm
from .filters import TransactionHistoryFilter
from .decorators import unauthenticated_user

############ AUTH PAGES URL ############

@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for {}'.format(user))
            return redirect('login')
        else:
            messages.info(request, form.errors)

    return render(request, 'auth/register.html', {'form': form})

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'auth/login.html', {})

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

############ MAIN PAGES URL ############

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html', {})

@login_required(login_url='login')
def transaction_history(request):
    transaction_history_data = TransactionHistory.objects.all()

    historyFilter = TransactionHistoryFilter(request.GET, queryset=transaction_history_data)
    transaction_history_data = historyFilter.qs

    context = {
        'history': transaction_history_data,
        'historyFilter': historyFilter,
    }

    return render(request, 'transaction_history.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def settings(request):
    ticker_form = TickerForm()
    ticker_currency_arr = TickerData.objects.all()

    context = {
        'ticker_form': ticker_form,
        'ticker_currency_arr': ticker_currency_arr
    }

    return render(request, 'settings.html', context)

############ BACKEND URL ############

@login_required(login_url='login')
@require_http_methods(['POST'])
def add_ticker(request):
    form = TickerForm(request.POST)
    if form.is_valid():
        ticker = TickerData(**form.cleaned_data)
        ticker.save()
    else:
        messages.error(request, form.errors)

    return redirect('settings')

@login_required(login_url='login')
@require_http_methods(['POST'])
def delete_ticker(request):
    for pk in request.POST.getlist('ticker_check'):
        ticker = get_object_or_404(TickerData, pk=pk)
        ticker.delete()

    return redirect('settings')

@login_required(login_url='login')
def delete_transaction_history(request, pk):
    transation = get_object_or_404(TransactionHistory, pk=pk)
    transation.delete()

    return redirect('transaction_history')
