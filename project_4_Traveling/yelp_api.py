
from urllib import response
from wsgiref import headers
import requests
import os
import time
from datetime import date,datetime
import datetime
import json

yelp_url = 'https://api.yelp.com/v3/events'
yelp_key = os.environ.get('YELP_API_KEY')

# Split each piece into smaller functions
def get_travel_info(destin_country, destin_city,destin_from_date, destin_to_date):
    #dates
    unix_from_time = generate_unix_from_date(destin_from_date)

    unix_to_time = generate_unix_to_date(destin_to_date)

    headers = generate_headers()

    params = generate_params(destin_city, destin_country,unix_from_time,unix_to_time)

    yelp_response = make_yelp_request(yelp_url, headers, params)

    yelp_3_events_descriptions = data_presentation_yelp(yelp_response)



    return yelp_3_events_descriptions
def generate_headers():
    headers = {
        'Authorization': 'Bearer ' + yelp_key 
    }
    return headers

def generate_params(destin_city, destin_country,unix_from_time,unix_to_time):
    params = {
        'location': destin_city + ', ' + destin_country,
        'limit': 3,
        'start_date':unix_from_time,
        'end_date':unix_to_time
    }
    return params

def make_yelp_request(yelp_url, headers, params):
    yelp_response = requests.get(yelp_url,headers=headers, params=params)
    # proceed only if the status code is 200
    print_yelp_status(yelp_response)
    return yelp_response

def print_yelp_status(response):
    print('The status code is {}'.format(response.status_code))

def generate_unix_from_date(destin_from_date):
    from_dates=destin_from_date.split("-")

    f_date= from_dates[2]
    f_month= from_dates[1]
    f_year= from_dates[0]

    from_date_constructor = f_date +'/'+ f_month + '/'+f_year

    unix_from_time= int(time.mktime(datetime.datetime.strptime(from_date_constructor,"%d/%m/%Y").timetuple()))
    return unix_from_time

def generate_unix_to_date(destin_to_date):
    t_dates=destin_to_date.split("-")

    t_date= t_dates[2]
    t_month= t_dates[1]
    t_year= t_dates[0]

    t_date_constructor = t_date +'/'+ t_month + '/'+t_year

    unix_to_time= int(time.mktime(datetime.datetime.strptime(t_date_constructor,"%d/%m/%Y").timetuple()))
    return unix_to_time

def data_presentation_yelp(yelp_response):
    # printing the text from the response 
    parsed_yelp_result = json.loads(yelp_response.text)
    #print(json.dumps(parsed_yelp_result, indent=4))
    #print(yelp_response)
    #print(yelp_response.keys())
    events = parsed_yelp_result["events"]
    total = parsed_yelp_result["total"]
    yelp_3_events_descriptions =list()
    
    #print(total)
    if total != 0:
        for event in events:
            #print(events)
            #print(event)
            #print(event[0].items())
            #print(event[0].title())
            name=event["name"]
            
            description=event["description"]
            
            image_yelp = event["image_url"]
            date =(event["time_start"])
           
            address = " ".join(event["location"]["display_address"])
            
            yelp_event_total_description=f'{name}. At {date}. Address: {address}'
            #print(yelp_event_total_description)
        
                      
            yelp_3_events_descriptions.append(yelp_event_total_description)

        #print(yelp_3_events_descriptions)
        #print(names)
  
        return yelp_3_events_descriptions
    else:
        return('')
    
   
            