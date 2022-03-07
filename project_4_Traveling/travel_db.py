"""
Project4 SQLite Andrew Abbe Daria K  Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James
 
"""
from email import message
import sqlite3

db = 'My_Travel_Events.sqlite'  # create datbase and variable is assigned.

class MyTravelEventDB():

    def create_table():
        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS MyTravelEvent (id int, event_name TEXT UNIQUE NOT NULL, event_date DATE, country text, city text, currency text)')
        #need to have:IF NOT EXISTS for tables and DB's. THis program 
        conn.close() 


    def display_all_records():
        conn = sqlite3.connect(db)  # connects datbase link
        results = conn.execute('SELECT * FROM MyTravelEvent')  #calls for all records from db for table jugglers 
        #message('\nAll event records:\n ')
        for row in results:
            print(row)
        conn.close()


    def search_records_by_name():
        try:
            search_name = input('enter new event name: ')
            search_cases = search_name.lower() 
            conn = sqlite3.connect(db)
            results = conn.execute('SELECT * FROM MyTravelEvent WHERE name like ?', (search_cases, ))
            first_row = results.fetchone()
            for row in first_row:
                    print('\nYour evnet name: ', row)                     
        except:
            print('\nnot found in database')   
                
        conn.close()
        

    def add_new_record():                
            new_name = input('enter new event name: ')
            new_country = input('enter Country name: ')
            new_catch_count = int(input('enter currency used: ')) 
            #addsnew reords to db, duplicate check in row with select query to db, tells user name, menu reloads. 
            with sqlite3.connect(db) as conn:
                try:
                    row_add = conn.execute('SELECT * FROM MyTravelEvent WHERE name like ?', (new_name,))
                    first_row = row_add.fetchone()
                    if first_row:
                        print(new_name, '\'s event is in our db already!')                        
                    else:
                        conn.execute('INSERT INTO MyTravelEvent VALUES (?, ?, ?)', (new_name, new_country, new_catch_count) )
                        print(new_name, '\'s name has added to our db.')
                except ValueError:                   
                    print('invalid') 

                conn.close()

    ## TODO
    def edit_existing_record():
        edit_name = input('Please enter the name of the event you want to edit: ')  # getting name for edit
        edit_ = input('enter new data: ')  # getting the new record unbmer for updating
        while True:  # needs to check number is an int
            if edit_event_id.isnumeric() is False:
                edit_event_id = input('Please enter a  ')  # TODO 
            else:
                break   
        edit_event_id = int(edit_event_id)           
        with sqlite3.connect(db) as conn:
            try:                  
                conn.execute('UPDATE MyTravelEvent SET '' = ? WHERE eventID = ?', (   ))
            except:
                print('record does not exist')  
            # edits an existing record. message passed if user wants to edit record that does not exist?'
        conn.close()

    ##TODO  name or ID
    # deletes existing record. What if user wants to delete record that does not exist?
    def delete_record():
        delete_name = input('enter event name to delete: ')
        delete_event = delete_event.lower()     
        with sqlite3.connect(db) as conn:
            try:                 
                for row in conn.execute('SELECT * FROM MyTravelEvent WHERE lower(name) like ?', (delete_event, )):
                    conn.execute('DELETE FROM MyTravelEvent WHERE name = ? ', (row[0],  ))
                    message('\nYour EVENT:', delete_event, 'was deleted, \nplease use menu to list all to verify.')           
            except Exception as e:                   
                    message('\nnot found in database', e)             
            #currently only exact match deletes record, update with any case entery sqlite does care case.   
        conn.close()


    def message(msg): 
        """ Prints a message for the user
        :param msg: the message to print"""
        print(msg)  # pass print statements.


    class RecordError(Exception):
        pass

   
# if __name__ == '__main__':
#     main()



 
        










# if __name__ == '__main__':
#     main()