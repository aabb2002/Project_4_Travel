# Andrew's portion
from urllib import response
import requests
import os
import time
from datetime import date
import datetime


weather_url = 'https://api.openweathermap.org/data/2.5/onecall'
yelp_url = 'https://api.yelp.com/v3/events'
currency_convertor_url = 'https://free.currconv.com/api/v7/convert'
geocoder_url = 'http://api.openweathermap.org/geo/1.0/direct'

weather_key = os.environ.get('WEATHER_API_KEY')
yelp_key = os.environ.get('YELP_API_KEY')
currency_convertor_key = os.environ.get('EXCHANGE_RATE_KEY')


def get_travel_info(destin_country, destin_city,destin_from_date,destin_to_date):

    from_dates=destin_from_date.split("-")

    f_date= from_dates[2]
    f_month= from_dates[1]
    f_year= from_dates[0]

    from_date_constructor = f_date +'/'+ f_month + '/'+f_year

    unix_from_time= int(time.mktime(datetime.datetime.strptime(from_date_constructor,"%d/%m/%Y").timetuple()))

    t_dates=destin_to_date.split("-")

    t_date= t_dates[2]
    t_month= t_dates[1]
    t_year= t_dates[0]

    t_date_constructor = t_date +'/'+ t_month + '/'+t_year

    unix_to_time= int(time.mktime(datetime.datetime.strptime(t_date_constructor,"%d/%m/%Y").timetuple()))

    headers = {
        'Authorization': 'Bearer ' + yelp_key 
    }
    params = {
        'location': destin_city + ', ' + destin_country,
        'limit': 3,
        'start_date':unix_from_time,
        'end_date':unix_to_time
    }

    api_response = requests.get(yelp_url,headers=headers, params=params).json()

    datalist =  api_response['events']
    
    for data in datalist:
        #print(datalist[data])
        print(data)
        event_name = [14]
        print(event_name)
        event_description = ['description']
        event_url = ['event_site_url']
        start_event_date = ['time_start']
        event_total = f'{event_name}: {event_description}. Event starts on {start_event_date} \n URL: {event_url}'
        return event_total


def get_conversion_rate(destin_currency,base_currency):
    params = {
        'apiKey': currency_convertor_key,
        'q': base_currency + "_" + destin_currency,
        'compact': 'ultra'
    }
    conversion_response = requests.get(currency_convertor_url, params).json()
    for rate in conversion_response.items():
        return(rate[1])
        


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

    forecast_response = requests.get(weather_url, params=params)
    data = forecast_response.json()
    #weather=data['daily'][0]['temp']['day']
    weather=data['current']
    temp= weather['temp']
    wind = weather['wind_speed']
    #inter = weather['weather']
    #description = inter['0']['description']
    
    weather_total = f'Currently it is {temp}F. Wind speed is {wind} mph.'
    #Can be described as {description}'
    #TODO: 

    return weather_total


def convert_location_to_lat_and_lon(destin_city, destin_country):

    params = {
        'q' : f'{destin_city},{destin_country}', 
        'appid': weather_key, 
        'limit': 1
    }

    lat_and_lon_response = requests.get(geocoder_url, params=params).json()

    latitude = lat_and_lon_response[0]['lat']
    longitude = lat_and_lon_response[0]['lon']
    return latitude, longitude