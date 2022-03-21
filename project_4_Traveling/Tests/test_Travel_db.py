import sqlite3
import unittest
from unittest import TestCase
import os 
import travel_db
from travel_db import Event, MyTravelEvents , RecordError

class TestTravelDB(TestCase):
    
    @classmethod
    def setUpClass(cls):
        travel_db = os.path.join('Tests', 'test_My_Travel_Events.sqlite')
        MyTravelEvents.instance = None


    def setup(self):
        self.db = MyTravelEvents()     
        self.clear_()


    def add_test_data(self):
        self.clear_db()

        self.ev1 = Event("Birthday", "2022-04-15 12:00:00" , "USA", "Minneapolis", "EUR", 78)
        self.ev2 = Event("Wedding", "2022-01-06 12:00:00" , "USA", "Minneapolis", "EUR", 88)
        self.ev3 = Event("Beach Party", "2022-01-06 12:00:00" , "USA", "San Diego", "USD", 98)    

        self.ev1.save()
        self.ev2.save()
        self.ev3.save()


    def test_add_event(self):
        self.add_test_data()
        event = self.add.event("Birthday", "2022-04-15 12:00:00" , "USA", "Minneapolis", "EUR", 78)
        event.save()
        self.assertEqual(3, event)    


    def test_get_all_events(self):
        self.add_test_data()
        self.assertCountEqual([self.ev1, self.ev2, self.ev3], self.test_get_all_events())

    def test_is_data_in_database(self):
        self.add_test_data()
        self.assertTrue(self.travel_db.exact_match(self.ev1))
        self.assertTrue(self.travel_db.exact_match(self.ev1))
        self.assertTrue(self.travel_db.exact_match(self.ev1))

   
    

