from urllib import response
import requests
import os
import time
from datetime import date, datetime

currency_convertor_url = 'https://free.currconv.com/api/v7/convert'
currency_convertor_key = os.environ.get('EXCHANGE_RATE_KEY')

class Request_Exception(Exception):
    pass

def get_conversion_rate(destin_currency):

    params = generate_request_params_for_currency(destin_currency)
    
    conversion_response = make_currency_requests(currency_convertor_url, params)

    return conversion_response


def generate_request_params_for_currency(destin_currency):

    params = {
        'apiKey' : currency_convertor_key,
        'q': "USD_" + destin_currency,
        'compact': 'ultra'
    }
    return params


def make_currency_requests(currency_convertor_url, params):
    try:
        conversion_response = requests.get(currency_convertor_url, params).json()
    except Exception as ex:
        print(ex)
        if conversion_response['status'] == 400:
            error_message = conversion_response['error']
        raise Request_Exception(error_message)

    print(conversion_response)
    
    for rate in conversion_response.items():
        return(rate[1])
