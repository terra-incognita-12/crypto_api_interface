import imp
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    
    path('transaction_history/', transaction_history, name='transaction_history'),
    path('transaction_history/delete/<str:pk>', delete_transaction_history, name='delete_transaction_history'),

    path('regular_trade/', trade_regular_trade, name='trade_regular_trade'),
    path('calculator/', trade_calculator, name='trade_calculator'),
    path('settings/', settings, name='settings'),
]