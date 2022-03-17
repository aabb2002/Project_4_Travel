import sqlite3
from datetime import date
import os

db = 'My_Travel_Events.sqlite'  # create datbase and variable is assigned.


class Event:
    def __int__(self, event_name, country, city, currency):
        self.event_name = event_name
        self.date = date
        self.country = country
        self.city = city
        self.currency = currency

        self.myTravelEvent = MyTravelEvent()

    def save_event(self):
        if self.event_name:
            self.myTravelEvent._add_event(self)


class MyTravelEvent:

    """ class to hold and manage a list of event. All database objects created are the same object.
    Provides operations to create database add, display/query the database.need to have: IF NOT EXISTS for tables and DB's. """



    def __init__(self):
        create_table_sql = 'CREATE TABLE IF NOT EXISTS Events (event_name TEXT UNIQUE NOT NULL, event_date DATE, country text, city text, currency text)'
                                 
        con = sqlite3.connect(db)
        
        with con:
            con.execute(create_table_sql)

        con.close()

    def get_all_events(self):
        """ returns an events list """

        get_all_events_sql = 'SELECT rowid, * FROM Events'

        con = sqlite3.connect(db)
        con.row_factory = sqlite3.Row
        rows = con.execute(get_all_events_sql)
        events = []

        for r in rows:
            event = Event(r['event_name'], r['Date'], r['country'], r['city'], r['temp'], r['curency'])
            event.append(event)

        con.close()            # reading list example book object event object.
        
        return events  

 
    # def _add_event(self)  #  save file                
    #         new_name = input('enter an event name: ') # add book example  weather save a highlight like average temp example.
    #         new_date = input('enter a Date : ')
    #         new_country = input('enter a Country name: ')
    #         new_city = input('enter a City name: ')
    #         new_currency= int(input('enter three letter currency code: '))
    #         #addsnew reords to db, duplicate check in row with select query to db, tells user name, menu reloads. 
    #         with sqlite3.connect(db) as conn:
    #             try:  # validateoin for event in db, checking by event_name. Possbly to same name multplie dates like  a festiville over severakl days.                     
    #                 row_add = conn.execute('SELECT * FROM MyTravelEvent WHERE event_name like ?', (new_name,))
    #                 first_row = row_add.fetchone()
    #                 if first_row:
    #                     print(new_name, '\'s event is in our db already!')                        
    #                 else:                               
    #                     conn.execute('INSERT INTO MyTravelEvent VALUES (?, ?, ?, ?, ?)', (new_name, new_date, new_country, new_city, new_currency ) )
    #                     print(new_name, '\'s name has added to our db.')
    #             except ValueError:                   
    #                 print('invalid') 
    #             conn.close()


class RecordError(Exception):
    pass

