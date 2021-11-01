from rest_framework import serializers 
from .models import ExchangeInfo
 
 
class ExchangeInfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ExchangeInfo
        fields = ('id',
                  'currency_code_from',
                  'currency_name_from',
                  'currency_code_to',
                  'currency_name_to',
                  'exchange_rate',
                  'last_refreshed',
                  'time_zone',
                  'bid_price',
                  'ask_price')