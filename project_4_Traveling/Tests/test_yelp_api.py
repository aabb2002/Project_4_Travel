from unittest import TestCase 
from unittest.mock import patch
from urllib import request, response
import currency_api
import yelp_api
import requests

class TestAPI(TestCase):

    def test_generate_params(self):
        params = yelp_api.generate_params('minneapolis', 'us', 1648093399, 	1648629789)
        self.assertEqual(params,{
        'location': 'minneapolis' + ', ' + 'us',
        'limit': 3,
        'start_date':1648093399,
        'end_date':1648629789
    })

    @patch('builtins.print')
    def test_print_status_code_for_successful_request(self, mock_print):
        params = {
            'location': 'minneapolis' + ', ' + 'us',
            'limit': 3,
            'start_date':1648093399,
            'end_date':1648629789
        }

        headers = {
            'Authorization': 'Bearer ' + yelp_api.yelp_key 
        }
        response = requests.get(yelp_api.yelp_url, headers=headers, params=params)
        yelp_api.print_yelp_status(response)
        mock_print.assert_called_once_with('The status code is 200')

    
    def test_generate_unix_time(self):
        unix_time = yelp_api.generate_unix_from_date('2022-03-24')
        self.assertEqual(unix_time, 1648098000)
