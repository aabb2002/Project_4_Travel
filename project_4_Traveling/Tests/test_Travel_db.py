import sqlite3
import unittest
from unittest import TestCase

import travel_db
from travel_db import RecordError

class TestTravelDB(TestCase):

    test_db_url = 'test_travel.db'

    def setUp(self):
        pass