import sqlite3
import os

db = 'My_Travel_Events.sqlite'  # create datbase and variable is assigned.

class Event:
    def __init__(self, country, city,event_name):
        self.country = country
        self.city = city
        self.event_name = event_name

        self.myTravelEvent = MyTravelEvents()


   
    def __str__(self):
        return f"{self.event_name=} {self.country=} {self.city=}"    


    def __eq__(self, other):
        return self.event_name == other.event_name and self.country == other.country and self.city == other.city 
        #  
    
    
    def __ne__(self, other):
        return self.event_name == other.event_name and self.country == other.country and self.city == other.city 
        


    def save_event(self):
        if not self.event_name:
             raise RecordError('Event does not have data, can\'t add')
        elif self.event_name:
            self.myTravelEvent.add_event(self)



class MyTravelEvents:

    """ class to hold and manage a list of event. All database objects created are the same object.
    Provides operations to create database add, display/query the database. need to have a command:
    "IF NOT EXISTS for tables and DB's." """


    def __init__(self):
        
        create_table_sql = 'CREATE TABLE IF NOT EXISTS Events (event_name TEXT NOT NULL,country text, city text)'
                                 
        con = sqlite3.connect(db)
        
        with con:
            con.execute(create_table_sql)


    def get_all_events(self):
        """ returns an events list """

        get_all_events_sql = 'SELECT * FROM Events'

        con = sqlite3.connect(db)
        con.row_factory = sqlite3.Row
        rows = con.execute(get_all_events_sql)
        events = []
        for r in rows:
            event = Event(r['event_name'], r['country'], r['city'])
            events.append(event)
                        
            con.close()            
            return events  

 
    def add_event(self, event):
        """save button - Adds event to database. Raises RecordError if 
        a event is already in the database (event_name unique.)  """     
        
        event_insert_sql = 'INSERT INTO Events (event_name, country, city) VALUES (?, ?, ? )'   
               
        try: 
            with sqlite3.connect(db) as con:                   
                res = con.execute( event_insert_sql, (event.event_name, event.country, event.city) )                              
        except sqlite3.IntegrityError as e:
            raise RecordError(f'Error - this event is already in the database. {event}') from e
        finally:
            con.close()


    def delete_events_all(self):
            '''deleting all the events from Events table'''
            delete_all_sql = 'DELETE from Events'
            with sqlite3.connect(db) as con:
                deleted = con.execute(delete_all_sql)
            con.close()


    def delete_events_all(self):
        '''deleting all the events from Events table'''
        delete_all_sql = 'DELETE from Events'
        with sqlite3.connect(db) as con:
            deleted = con.execute(delete_all_sql)

        con.close()


class RecordError(Exception):
    pass
