from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime
from celery.utils.log import get_task_logger
from dotenv import load_dotenv
import requests
import os
import json
#from .views import get_exchangelist
load_dotenv()
shared_task(name="store_exchange_info")
def store_exchange_info():
    apikey=os.environ.get('api_key')
    print(apikey)
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey='+apikey
    r = requests.get(url)
    data = r.json()
    params=data['Realtime Currency Exchange Rate']
    send_request={
        'currency_code_from':params['1. From_Currency Code'],
                  'currency_name_from':params['2. From_Currency Name'],
                  'currency_code_to':params['3. To_Currency Code'],
                  'currency_name_to':params['4. To_Currency Name'],
                  'exchange_rate':params['5. Exchange Rate'],
                  'last_refreshed':params['6. Last Refreshed'],
                  'time_zone':params['7. Time Zone'],
                  'bid_price':params['8. Bid Price'],
                  'ask_price':params['9. Ask Price']
                  
    }
    
    posturl="http://api:5050/api/v1/quotes"
    
    payload = json.dumps(send_request)
    headers = {'content-type': 'application/json'}
    result=requests.post(posturl,data=payload,headers=headers).json()
    print(result)