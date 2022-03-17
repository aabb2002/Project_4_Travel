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

 
    def _add_event(self)  #  save button """ Adds evnet to database. Raises RecordError if a event wit (not case sensitive) is already in the database."""   
        insert_sql = 'INSERT INTO Events (event_name, date, country, city, currency, temp) VALUES (?, ?, ?, ?, ?, ?)'
        try: 
            with sqlite3.connect(db) as con:
                res = con.execute(insert_sql, (event_name.n) )
                new_event_name = res.lastrowid  # Get the ID of the new row in the table 
                event_name = new_event_name  # Set this book's ID
        except sqlite3.IntegrityError as e:
                raise RecordError(f'Error - this event is in the database. {event_name}') from e
        finally:
            con.close()


class RecordError(Exception):
    pass

