from email import header
from urllib import response
from wsgiref import headers
import requests
import os
import time
from datetime import date, datetime

yelp_url = 'https://api.yelp.com/v3/events'
yelp_key = os.environ.get('YELP_API_KEY')

# Split each piece into smaller functions
def get_travel_info(destin_country, destin_city):

    headers = generate_headers()

    params = generate_params(destin_city, destin_country)

    yelp_response = make_yelp_request(yelp_url, headers, params)
    return yelp_response

def generate_headers():
    headers = {
        'Authorization': 'Bearer ' + yelp_key 
    }
    return headers

def generate_params(destin_city, destin_country):
    params = {
        'location': destin_city + ', ' + destin_country,
        'limit': 3
    }
    return params

def make_yelp_request(yelp_url, headers, params):
    yelp_response = requests.get(yelp_url,headers=headers, params=params).json()
    return yelp_response