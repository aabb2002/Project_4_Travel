import sqlite3
from datetime import date


db = 'My_Travel_Events.sqlite'  # create datbase and variable is assigned.

class Event:
    def __int__(self, event_name, country, city, currency, current_temp):
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

    def main():
             
        with sqlite3.connect(db) as con:
            #keeping this for testing creating  table.
       
            con.execute('INSERT INTO Events VALUES ("Birthday", "2022-04-15" , "USA", Minneapolis, "EUR", 78')
            con.execute('INSERT INTO Events VALUES ("Wedding", "2022-04-01" , "USA", Minneapolis, "EUR", 88')
        con.close()  


    def __init__(self):
        create_table_sql = 'CREATE TABLE IF NOT EXISTS MyTravelEvent (event_name TEXT UNIQUE NOT NULL, event_date DATE, country text, city text, currency text, current_temp small int)'
                                 
        con = sqlite3.connect(db)
        
        with con:
            con.execute(create_table_sql)

        con.close()

    def get_all_events(self):
        """ returns an events list """

        get_all_events_sql = 'SELECT * FROM MyTravelEvent'

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
        """save button - Adds evnet to database. Raises RecordError if 
        a event wit (not case sensitive) is already in the database."""         
        
        with sqlite3.connect(db) as con:
            try:             
                row_add = con.execute('SELECT * FROM MyTravelEvent WHERE event_name like ?', (event,))
                first_row = row_add.fetchone()
                if first_row:
                    raise RecordError(f'Error - this event is in the database. {event}')                 
                else:
                    con.execute('INSERT INTO Events (event_name, date, country, city, currency, current_temp VALUES (?, ?, ?, ?, ?, ?')
            except ValueError as e:
                return(e)
            con.close()


class RecordError(Exception):
    pass



if __name__ == '__main__':
    main()