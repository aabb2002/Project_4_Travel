# Daria's portion
from flask import Flask, render_template, request
from project_4_Traveling.travel_APIs import get_weather_forecast
from travel_APIs import get_travel_info, get_conversion_rate
#from travel_APIs
import sqlite3 as sql

from project_4_Traveling.travel_db import MyTravelEventDB
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/destination_info') 
def get_travel_info():
    print(request.args)
    destin_city = request.args.get('destin_city')
    destin_country = request.args.get('destin_country')
    destin_currency = request.args.get('destin_currency')
    base_currency = request.args.get('base_currency')
    if (destin_country, destin_city,destin_currency,base_currency):
        userinfo = get_travel_info(destin_country, destin_city)
        conversion_rate = get_conversion_rate(destin_currency,base_currency)
        weather_forecast = get_weather_forecast(destin_country, destin_city)
        return render_template(
            'destination.html', 
            userinfo= userinfo, 
            conversion_rate=conversion_rate, 
            userinfo=userinfo,
            weather_forecast=weather_forecast)
    else:
        return "error"


@app.route('/saved_destinations')
def saved_travel_info():
    con = sql.connect("travel_db.py")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute(MyTravelEventDB.display_all_records)

    rows = cur.fetchall()
    return render_template("saved_destinations.html", rows = rows)


if __name__ == '__main__':
    app.run()