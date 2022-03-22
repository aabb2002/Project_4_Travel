
import sqlite3
import unittest
from unittest import TestCase
import os 
import travel_db
from travel_db import Event, MyTravelEvents , RecordError

class TestTravelDB(TestCase):
    
    @classmethod
    def setUpClass(cls):
        travel_db.db = os.path.join('Tests', 'test_My_Travel_Events.sqlite')
        MyTravelEvents.instance = None


    def setUp(self):
        self.MTE = MyTravelEvents()     
        self.clear_travel_db()


    def add_test_data(self):
        self.clear_travel_db()

        self.ev1 = Event("Birthday", "2022-04-15 12:00:00" , "USA", "Minneapolis", "EUR", 78)
        self.ev2 = Event("Wedding", "2022-01-06 12:00:00" , "USA", "Minneapolis", "EUR", 88)
        self.ev3 = Event("Beach Party", "2022-01-06 12:00:00" , "USA", "San Diego", "USD", 98)    

        self.ev1.save_event()
        self.ev2.save_event()
        self.ev3.save_event()


    def clear_travel_db(self):
        self.MTE.delete_events_all()


    def test_add_event(self):     
        self.clear_travel_db () 
        self.ev = Event("Fun Day", "2022-04-15 12:00:00" , "USA", "Minneapolis", "EUR", 78)
        self.ev.save_event()
        self.assertTrue([self.ev], self.MTE.get_all_events())
        #self.assertEqual([self.ev], self.MTE.get_all_events())
       

    def test_add_event_to_database_with_data(self):
        self.add_test_data()
        self.ev0 = Event("Concert", "2022-04-15 12:00:00", "USA", "Minneapolis", "EUR", 78)
        self.ev0.save_event()
        self.assertTrue(self.ev0, self.MTE.get_all_events())
        #self.assertCountEqual(4, self.MTE.get_all_events())            


    # def test_get_all_events(self):
    #     """test asserts to True but not to equal"""
    #     self.add_test_data()
    #     self.assertTrue([self.ev1, self.ev2, self.ev3], self.MTE.get_all_events())


    def test_is_data_in_database(self):
        """test working to add data and find data is in the database"""
        self.add_test_data()
        self.assertTrue(self.MTE.get_all_events())
        #self.clear_travel_db()


    def test_delete_all_events(self):
        self.add_test_data()
        self.MTE.delete_events_all()
        self.assertNotIn(0, self.MTE.get_all_events())        


       

   
    

