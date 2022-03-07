# Daria's portion
from flask import Flask, render_template, request
#from travel_APIs
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
    base_currency = request.args.get('base_currecny')
    if (destin_country, destin_city,destin_currency,base_currency):
        userinfo = get_travel_info(destin_country, destin_city,destin_currency,base_currency)
        return render_template('', userinfo= userinfo)
    else:
        return "error"

if __name__ == '__main__':
    app.run()