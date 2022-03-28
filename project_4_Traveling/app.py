# Daria's portion

from flask import Flask, render_template, request,redirect, url_for


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
        yelp_3_events_descriptions = get_travel_info(destin_country, destin_city,destin_from_date,destin_to_date)
        #names_event = get_travel_info(destin_country, destin_city,destin_from_date,destin_to_date)
        conversion_rate = get_conversion_rate(destin_currency)
        weather_7_days = get_weather_forecast(destin_country, destin_city)
        conversion_rate_rounded = round(conversion_rate,2)
        

        return render_template(
            'destination_info.html', 
            destin_city=destin_city,
            destin_country=destin_country,
            destin_from_date=destin_from_date,
            destin_to_date=destin_to_date,
            destin_currency = destin_currency,
            conversion_rate=conversion_rate_rounded, 
            weather_7_days = weather_7_days,
            yelp_3_events_descriptions=yelp_3_events_descriptions)
            #names_event = names_event)
    

    else:
        return "Please fill out all the fields"

@app.route('/saveuserinfo',methods=['POST'])
def saveuserinfo():
    for i in range (1,3):
        country = request.form.get('country')
        city = request.form.get('city')

        event_name = request.form.get('event')
    #destin_from_date = request.form.get('destin_from_date')
    #destin_to_date = request.form.get('destin_to_date')
        print(city, country,event_name)
        save_event_flask = Event(event_name,country,city)
        save_event_flask.save_event()
    return ('Success')
   # return render_template('saved_destinations.html', saved=saved)

@app.route('/saveduserinfo',methods=['GET'])
#@app.route('/show_saved')
def show_saved_destinations():
    # get destinations from the database 
    #saved = MyTravelEvents()
    #show_events = []
    show_events = MyTravelEvents.get_all_events()
    print(show_events)
    #for i in show_events:
    #TODO database object to show on the screen
    return render_template('saved_destinations.html', show_events = show_events)
    
    



