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
        self.events = MyTravelEvents()     
        self.clear_travel_db()


    def add_test_data(self):
        self.clear_travel_db()

        self.ev1 = Event("Birthday", "2022-04-15 12:00:00" , "USA", "Minneapolis", "EUR", 78)
        self.ev2 = Event("Wedding", "2022-01-06 12:00:00" , "USA", "Minneapolis", "EUR", 88)
        self.ev3 = Event("Beach Party", "2022-01-06 12:00:00" , "USA", "San Diego", "USD", 98)    

        self.ev1.save()
        self.ev2.save()
        self.ev3.save()


    def clear_travel_db(self):
        self.events.delete_all_events()


    def test_add_event(self):       
        ev = Event("Fun Day", "2022-04-15 12:00:00" , "USA", "Minneapolis", "EUR", 78)
        ev.save()
        self.assertTrue(self.events.exact_match(ev))
        self.assertEqual(1, ev)


    # def test_add_event_to__database_with_data(self):
    #     self.add_test_data()
    #     ev0 = Event("Concert", "2022-04-15 12:00:00" , "USA", "Minneapolis", "EUR", 78)
    #     ev0.save()
    #     self.assertTrue(self.Events.exact_match(ev0))
    #     self.assertEqual(1, ev0)            


    # def test_get_all_events(self):
    #     self.add_test_data()
    #     self.assertCountEqual([self.ev1, self.ev2, self.ev3], self.test_get_all_events())


    # def test_is_data_in_database(self):
    #     self.add_test_data()
    #     self.assertTrue(self.Events.exact_match(self.ev1))
    #     self.assertTrue(self.Events.exact_match(self.ev1))
    #     self.assertTrue(self.Events.exact_match(self.ev1))

   
    

