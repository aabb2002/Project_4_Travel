import sqlite3
from typing import Counter
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

        self.ev1 = Event("Birthday", "USA", "Minneapolis")
        self.ev2 = Event("Wedding", "USA", "Minneapolis")
        self.ev3 = Event("Beach Party", "USA", "San Diego")    

        self.ev1.save_event()
        self.ev2.save_event()
        self.ev3.save_event()


    def clear_travel_db(self):
        self.MTE.delete_events_all()


    def test_add_event(self):    
        """test is not working, test adds one event and checks database for event added to database""" 
        self.clear_travel_db () 
        new_event = Event("Fun Day", "USA", "Minneapolis")
        new_event.save_event()
        expected_single_event_from_db = self.MTE.get_all_events()
        self.assertEqual(1, len(expected_single_event_from_db))
        saved_event = expected_single_event_from_db[0]  # takes index position from list of variable called
        self.assertEqual(saved_event, new_event)
        self.assertEqual(saved_event.event_name, new_event.event_name)#created here is the same as the event in the database
        self.assertEqual(saved_event.country, new_event.country)  # event created here is the same as the event in the database
        self.assertEqual(saved_event.city, new_event.city)  # event created here is the same as the event in the database


    def test_add_event_duplicate(self):
        """test is working"""
        self.clear_travel_db () 
        self.ev = Event("Hockey Day", "USA", "Minneapolis")   
        self.ev.save_event()
        with self.assertRaises(RecordError):
            self.dup = Event("Hockey Day", "USA", "Minneapolis") 
            self.dup.save_event()


    def test_add_event_to_database_with_data(self):
        """test working, test adds test date events plu one event and checks database for events added"""   
        self.add_test_data()
        next_event = Event("UHL Hockey", "UKR", "Ukrainian")
        next_event.save_event()
        expected_list_from_db = self.MTE.get_all_events()
        self.assertEqual(4, len(expected_list_from_db))  # 3 is for evnets entered
        self.assertEqual([self.ev1, self.ev2, self.ev3, next_event], expected_list_from_db)            


    def test_get_all_events(self):
        """test not working, asserts to True but not to equal"""
        self.clear_travel_db
        self.add_test_data()
        self.assertEqual([self.ev1, self.ev2, self.ev3], self.MTE.get_all_events())


    def test_is_data_in_database(self):
        """test working to add data and finds data is in the database"""
        self.add_test_data()
        self.assertTrue(self.MTE.get_all_events())
        #self.clear_travel_db()


    def test_delete_all_events(self):
        """tests working, it test that delete_events is deleting data."""
        self.add_test_data()
        self.MTE.delete_events_all()
        self.assertEqual([], self.MTE.get_all_events())   


    def test_add_event_no_event(self):
        """test is working, raising error if data is not present"""
        self.clear_travel_db()
        empty = Event("","","","") 
        with self.assertRaises(RecordError):
            empty.save_event()


       

   
    

