from django.db import models

class ExchangeInfo(models.Model):
    id = models.AutoField(primary_key=True)
    currency_code_from = models.CharField(max_length=100)
    currency_name_from = models.CharField(max_length=100)
    currency_code_to = models.CharField(max_length=100)
    currency_name_to = models.CharField(max_length=100)
    exchange_rate=models.DecimalField(max_digits=20, decimal_places=10)
    last_refreshed=models.DateTimeField(auto_now_add=True)
    time_zone=models.CharField(max_length=50)
    bid_price=models.DecimalField(max_digits=20, decimal_places=10)
    ask_price=models.DecimalField(max_digits=20, decimal_places=10)