from urllib import response
import requests
import os
import time
from datetime import date, datetime

weather_url = 'https://api.openweathermap.org/data/2.5/onecall'
geocoder_url = 'http://api.openweathermap.org/geo/1.0/direct'

weather_key = os.environ.get('WEATHER_API_KEY')

def get_weather_forecast(destin_country, destin_city):

    lat_and_lon = convert_location_to_lat_and_lon(destin_city, destin_country)

    params = {
        'lat': lat_and_lon[0], 
        'lon': lat_and_lon[1], 
        'units': 'imperial', 
        'appid': weather_key, 
        'exclude': 'minutely, hourly, alerts',
        'units': 'imperial'
    }

    forecast_response = requests.get(weather_url, params=params).json()

    return forecast_response


def convert_location_to_lat_and_lon(destin_city, destin_country):

    params = generate_request_params_for_location(destin_city, destin_country)
    
    # 2. making a request to the api - mocking may be needed here
    places_location_response = make_geocode_request(geocoder_url, params)
    
    # 3. getting data from the response - 
    # TODO what if no data is returned? What does this do?
    # TODO what about no connection, server error? 
    latitude, longitude = get_first_place_lat_lon(places_location_response)
    
    return latitude, longitude


def generate_request_params_for_location(city, country):
    # todo validate data? - 
    # 1. generating parameters dictionary 
    params = {
        'q' : f'{city},{country}', 
        'appid': weather_key,   
        'limit': 1
    }
    return params


# todo mock this part 
def make_geocode_request(geocoder_url, params):
    places_location_response = requests.get(geocoder_url, params=params).json()
    return places_location_response


def get_first_place_lat_lon(places_location_response):
    # todo error handling - what list is empty? 
    latitude = places_location_response[0]['lat']
    longitude = places_location_response[0]['lon']
    return latitude, longitude