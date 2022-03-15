
import sqlite3

db = 'My_Travel_Events.sqlite'  # create datbase and variable is assigned.

class MyTravelEventDB():

    def create_table():  # currency is acronym args for countries
        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS MyTravelEvent (id int, event_name TEXT UNIQUE NOT NULL, event_date DATE, country text, city text, currency text)')
        #need to have:IF NOT EXISTS for tables and DB's.
        conn.close() 


    def display_all_records():  # records for travel from bookmark/saved data.
        conn = sqlite3.connect(db)  # connects datbase link
        results = conn.execute('SELECT * FROM MyTravelEvent')  #calls for all records from db 
        #message('\nAll event records:\n ')
        for row in results:
            print(row)
        conn.close()


    def search_records_by_name():  # setup id for searches/possbile change for event name.
        try:
            event_name = input('enter new event name: ')
            if event_name < 0:           
                raise RecordError('Provide a positive number')   
            conn = sqlite3.connect(db)
            results = conn.execute('SELECT * FROM MyTravelEvent WHERE event_id like ?', (event_name))
            first_row = results.fetchone()
            for row in first_row:
                    print('\nYour evnet name: ', row)                     
        except:
            print('\nnot found in database')                   
        conn.close()
        

    def add_new_record():  #  save file                
            new_name = input('enter an event name: ')
            new_date = input('enter a Date : ')
            new_country = input('enter a Country name: ')
            new_city = input('enter a City name: ')
            new_currency= int(input('enter three letter currency code: '))
            #addsnew reords to db, duplicate check in row with select query to db, tells user name, menu reloads. 
            with sqlite3.connect(db) as conn:
                try:  # validateoin for event in db, checking by event_name. Possbly to same name multplie dates like  a festiville over severakl days.                     
                    row_add = conn.execute('SELECT * FROM MyTravelEvent WHERE event_name like ?', (new_name,))
                    first_row = row_add.fetchone()
                    if first_row:
                        print(new_name, '\'s event is in our db already!')                        
                    else:                               
                        conn.execute('INSERT INTO MyTravelEvent VALUES (?, ?, ?, ?, ?)', (new_name, new_date, new_country, new_city, new_currency ) )
                        print(new_name, '\'s name has added to our db.')
                except ValueError:                   
                    print('invalid') 
                conn.close()


    # deletes existing record. What if user wants to delete record that does not exist?
    def delete_record():
        delete_event = input('enter event name to delete: ')
        delete_event = delete_event.lower()     
        with sqlite3.connect(db) as conn:
            try:                 
                for row in conn.execute('SELECT * FROM MyTravelEvent WHERE lower(name) like ?', (delete_event, )):
                    conn.execute('DELETE FROM MyTravelEvent WHERE name = ? ', (row[0],  ))
                    print('\nYour EVENT:', delete_event, 'was deleted, \nplease use menu to list all to verify.')           
            except Exception as e:                   
                    print('\nnot found in database', e)             
            #currently only exact match deletes record, update with any case entery sqlite does care case.   
        conn.close()


class RecordError(Exception):
    pass

