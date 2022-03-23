# Daria's portion
from argparse import Action
from multiprocessing import Event
from flask import Flask, render_template, request, redirect
from currency_api import get_conversion_rate

from weather_api import get_weather_forecast
from yelp_api import get_travel_info

import sqlite3 as sql
from travel_db import MyTravelEvents
from travel_db import Event

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/getuserinfo') 
def myTravelEventInfo():
    print(request.args)
    # city, country info from HTML user inputs on homepage.html
    destin_city = request.args.get('destin_city')
    destin_country = request.args.get('destin_country')

    # To and om dates in mm/dd/yyyy format from HTML user inputs on homepage.html
    destin_from_date=request.args.get('destin_from_date')
    destin_to_date=request.args.get('destin_to_date')

    # destination currency (abbreviated) from the HTML user input on homepage.html
    destin_currency = request.args.get('destin_currency')
    #our base currency is USD but changing it to any other currency abbreviation would work the same
    #if changing, change the html homepage explanation to the user
    

    if (destin_country, destin_city, destin_from_date, destin_to_date, destin_currency):
        #userinfo = get_travel_info(destin_country, destin_city, destin_from_date, destin_to_date)
        yelp_3_events_descriptions  = get_travel_info(destin_country, destin_city,destin_from_date,destin_to_date)
        name = get_travel_info(destin_country, destin_city,destin_from_date,destin_to_date)

        # second_event = get_travel_info(destin_country, destin_city,destin_from_date,destin_to_date)
        # third_event = get_travel_info(destin_country, destin_city,destin_from_date,destin_to_date)
        conversion_rate = get_conversion_rate(destin_currency)
        #forecast_response = get_weather_forecast(destin_country, destin_city)
        # weather_total = get_weather_forecast(destin_country, destin_city)
        weather_7_days = get_weather_forecast(destin_country, destin_city)
        conversion_rate_rounded = round(conversion_rate,2)
        

        return render_template(
            'destination_info.html', 
            #userinfo= userinfo, 
            destin_city=destin_city,
            destin_country=destin_country,
            destin_currency = destin_currency,
            conversion_rate=conversion_rate_rounded, 
            #forecast_response= forecast_response,
            #forecast = forecast,
            # weather_total = weather_total, 
            weather_7_days = weather_7_days,
            #event_total= event_total,
            yelp_3_events_descriptions=yelp_3_events_descriptions, 
            name = name)




    else:
        return "error"

# Anything that modifies the database should use a POST request to make it harder for the 
# user to make multiple requests that do the same thing and end up with duplicate data
@app.route('/save', methods=['POST'])
def save():
    form_data = request.form 
    city = request.form.get('city')
    country = request.form.get('country')

    print(city, country)  # just to see that the data is available
    # etc.
    # save this to the database 
    # success? you can redirect to the home page, or the list of destinations, or show a new "success!" page, or whatever you like 
    return redirect('/show_saved')   # this will make a new request to the /show_saved route which will load all the destinations including the new one 
    # todo check DB response and show error page if error 



@app.route('/show_saved')
def show_saved_destinations():
    # get destinations from the database 
    destinations = []  # replace with destinations from DB
    return render_template('saved_destinations.html', destinations=destinations)




