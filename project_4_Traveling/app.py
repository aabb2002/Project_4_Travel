# Daria's portion
from flask import Flask, render_template, request
from currency_api import get_conversion_rate
from weather_api import get_weather_forecast
from yelp_api import get_travel_info

import sqlite3 as sql
from travel_db import MyTravelEventDB

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
    base_currency = 'USD'

    if (destin_country, destin_city, destin_from_date, destin_to_date, destin_currency):


        #userinfo = get_travel_info(destin_country, destin_city, destin_from_date, destin_to_date)
        event_total = get_travel_info(destin_country, destin_city, destin_from_date, destin_to_date)
        conversion_rate = get_conversion_rate(destin_currency,base_currency)
        #forecast_response = get_weather_forecast(destin_country, destin_city)
        weather_total = get_weather_forecast(destin_country, destin_city)
        conversion_rate_rounded = round(conversion_rate,2)

    if (destin_country, destin_city,destin_currency,base_currency):
        userinfo = get_travel_info(destin_country, destin_city)
        conversion_rate = get_conversion_rate(destin_currency)
        forecast_response = get_weather_forecast(destin_country, destin_city)

        return render_template(
            'destination_info.html', 
            #userinfo= userinfo, 
            destin_city=destin_city,
            destin_country=destin_country,
            destin_currency = destin_currency,
            conversion_rate=conversion_rate_rounded, 
            #forecast_response= forecast_response,
            #forecast = forecast,
            weather_total = weather_total, 
            event_total= event_total
            conversion_rate=conversion_rate, 
            forecast_response= forecast_response)

    else:
        return "error"


@app.route('/saved')
def saved_travel_info():
    # con = sql.connect('travel_db.py')
    # con.row_factory = sql.Row

    # cur = con.cursor()
    # cur.execute(MyTravelEventDB.display_all_records)

    # rows = cur.fetchall()
    return render_template('saved_destinations.html')
    #, MyTravelEventDB.display_all_records)


if __name__ == '__main__':
    app.run(debug = True)