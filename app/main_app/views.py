from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def transaction_history(request):
    return render(request, 'transaction_history.html', {})