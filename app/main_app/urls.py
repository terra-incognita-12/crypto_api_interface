import imp
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('transaction_history/', transaction_history, name='transaction_history'),
]