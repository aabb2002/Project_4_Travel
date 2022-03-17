# Andrew's portion
from urllib import response
import requests
import os
import time
from datetime import date, datetime

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
        'q': base_currency + "_" + destin_currency,
        'compact': 'ultra'
    }
    conversion_response = requests.get(currency_convertor_url, params).json()
    return conversion_response

# def get_location(destin_city, destin_country):
#     destin_city, destin_country = '',''
#     #question about notation above
#     location=f'{destin_city},{destin_country}'
#     return location


# def get_weather_forecast(location, weather_key):
#     try:
#         query={'q':location,'units':'metric', 'appid':weather_key}
#         response = requests.get(weather_url,params = query)
#         response.raise_for_status() #raise exception for 400 and 500 errors
#         data = response.json() #this may error too, if response is not json

#         list_of_forecast = data['list']
#         #print(list_of_forecast)
#         for forecast in list_of_forecast:
#             temp = forecast['main']['temp']
#             temp_round = round(temp)
#             timestamp=forecast['dt']
#             wind_speed = forecast['wind']['speed']
#             description = forecast['weather'][0]['description']
#             forecast_date = datetime.date.fromtimestamp(timestamp)
#             forecast_time = time.time()    
#         return forecast, None #data is a tuple
#     except Exception as e:
#         print(e)
#         #print(response.text) #added for debugging
#         return None, e #tuple will be none

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
def make_geocode_request(gecoder_url, params):
    places_location_response = requests.get(geocoder_url, params=params).json()
    return places_location_response


def get_first_place_lat_lon(places_location_response):
    # todo error handling - what list is empty? 
    latitude = places_location_response[0]['lat']
    longitude = places_location_response[0]['lon']
    return latitude, longitude