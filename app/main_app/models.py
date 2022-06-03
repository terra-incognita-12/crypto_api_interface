from pyexpat import model
from django.db import models

class TransactionHistory(models.Model):
    buy_currency = models.CharField(max_length=50)
    buy_currency_amount = models.FloatField()
    sell_currency = models.CharField(max_length=50)
    sell_currency_amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
