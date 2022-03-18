import sqlite3


db = 'My_Travel_Events.sqlite'  # create datbase and variable is assigned.


class Event:
    def __int__(self, event_name, date, country, city, currency, current_temp):
        self.event_name = event_name
        self.date = date
        self.country = country
        self.city = city
        self.currency = currency
        self.current_temp = current_temp

        self.myTravelEvent = MyTravelEvents()

    def save_event(self):
        if self.event_name:
            self.myTravelEvent.add_event(self)


class MyTravelEvents:

    """ class to hold and manage a list of event. All database objects created are the same object.
    Provides operations to create database add, display/query the database. need to have a command:
    "IF NOT EXISTS for tables and DB's." """


    def __init__(self):
        create_table_sql = 'CREATE TABLE IF NOT EXISTS Events (event_name TEXT UNIQUE NOT NULL, event_date DATE, country text, city text, currency text, current_temp small int)'
                                 
        con = sqlite3.connect(db)
        
        with con:
            con.execute(create_table_sql)

        con.close()


    def get_all_events(self):
        """ returns an events list """

        get_all_events_sql = 'SELECT * FROM Events'

        con = sqlite3.connect(db)
        con.row_factory = sqlite3.Row
        rows = con.execute(get_all_events_sql)
        events = []

        for r in rows:
            event = Event(r['event_name'], r['Date'], r['country'], r['city'], r['currency'], r['current_temp'])
            events.append(event)

        con.close()            #  example book object event object.
        return events  

 
    def add_event(self, event):
        """save button - Adds event to database. Raises RecordError if 
        a event is already in the database (event_name unique.) TODO - do we need to think about case? """     

        event_insert_sql = 'INSERT INTO Events (event_name, date, country, city, currency, current_temp VALUES (?, ?, ?, ?, ?, ?'      
               
        try: 
            with sqlite3.connect(db) as con:
                res = con.execute(event_insert_sql, (event.event_name, event.date, event.country, event.city, event.currency, event.current_temp ) )     
                new_id = res.lastrowid  # Get the ID of the new row in the table 
                event.event_name = new_id  # Set this event ID                  
        except sqlite3.IntegrityError as e:
            raise RecordError(f'Error - this event is already in the database. {event}') from e
        finally:
            con.close()
 

class RecordError(Exception):
    pass



