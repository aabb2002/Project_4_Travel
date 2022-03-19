from urllib import response
import requests
import os
import time
from datetime import date, datetime

currency_convertor_url = 'https://free.currconv.com/api/v7/convert'
currency_convertor_key = os.environ.get('EXCHANGE_RATE_KEY')

def get_conversion_rate(destin_currency):

    params = generate_request_params_for_currency(destin_currency)
    
    conversion_response = make_currency_requests(currency_convertor_url, params)

    return conversion_response


def generate_request_params_for_currency(destin_currency):

    params = {
        'apiKey': currency_convertor_key,
        'q': "USD_" + destin_currency,
        'compact': 'ultra'
    }
    return params


def make_currency_requests(currency_convertor_url, params):
    conversion_response = requests.get(currency_convertor_url, params).json()
    for rate in conversion_response.items():
        return(rate[1])
