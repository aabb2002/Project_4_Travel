# Daria's portion
from argparse import Action
from multiprocessing import Event
from flask import Flask, render_template, request
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

    def save(country, city,name):
            if request.method == 'GET':
                if request.form['save_button'] == 'SAVE':
                    destin_country=Event.country
                    destin_city= Event.city
                    name= Event.name
                    pass 
            elif request.form['Show_Saved'] == 'SHOW SAVED':
                    all_events = MyTravelEvents.get_all_events
                    return render_template('saved_destinations.html', all_events=all_events)
                    pass 
            else:
                pass 




