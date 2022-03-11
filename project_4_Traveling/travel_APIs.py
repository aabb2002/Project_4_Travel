# Andrew's portion
from urllib import response
import requests
import os

weather_url = 'https://api.openweathermap.org/data/2.5/onecall'
yelp_url = 'https://api.yelp.com/v3/events'
currency_convertor_url = 'https://free.currconv.com/api/v7/convert'
geocoder_url = 'http://api.openweathermap.org/geo/1.0/direct'

weather_key = os.environ.get('WEATHER_API_KEY')
yelp_key = os.environ.get('YELP_API_KEY')
currency_convertor_key = os.environ.get('EXCHANGE_RATE_KEY')


def get_travel_info(destin_country, destin_city):

    headers = {
        'Authorization': 'Bearer ' + yelp_key 
    }
    params = {
        'location': destin_city + ', ' + destin_country,
        'limit': 3
    }

    api_response = requests.get(yelp_url,headers=headers, params=params).json()
    return api_response


def get_conversion_rate(destin_currency,base_currency):

    params = {
        'apiKey': currency_convertor_key,
        'q': base_currency + '_' + destin_currency,
        'compact': 'ultra'
    }

    conversion_response = requests.get(currency_convertor_url, params).json()
    return conversion_response


def get_weather_forecast(destin_country, destin_city):

    lat_and_lon = convert_location_to_lat_and_lon(destin_city, destin_country)

    params = {
        'lat': lat_and_lon[0], 
        'lon': lat_and_lon[1], 
        'units': 'imperial', 
        'appid': weather_key, 
        'exclude': 'current, minutely, hourly, alerts',
        'units': 'imperial'
    }

    forecast_response = requests.get(weather_url, params=params).json()
    return forecast_response


def convert_location_to_lat_and_lon(destin_city, destin_country):

    params = {
        'q' : destin_city + ', ' + destin_country, 
        'appid': weather_key, 
        'limit': 1
    }

    lat_and_lon_response = requests.get(geocoder_url, params=params).json()

    latitude = lat_and_lon_response[0]['lat']
    longitude = lat_and_lon_response[0]['lon']
    return latitude, longitude