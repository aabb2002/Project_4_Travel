from unittest import TestCase 
from unittest.mock import patch
from urllib import response
from webbrowser import get
import currency_api

class TestAPI(TestCase):

    def test_generate_currency_parameters(self):
        params = currency_api.generate_request_params_for_currency('eur')
        self.assertEqual(params, {
        'apiKey': currency_api.currency_convertor_key,
        'q': "USD_eur",
        'compact': 'ultra'
    })

    @patch('currency_api.get_conversion_rate', return_value = .9)
    def test_currency_response(self, mock_response):
        conversion_response = currency_api.get_conversion_rate('EUR')
        self.assertEqual(conversion_response, 0.9)
    
    def test_raise_request_exception_with_wrong_url(self):
        broke_url = 'https://www.notworking.gov'
        params = {
            'apiKey': currency_api.currency_convertor_key,
            'q': "USD_eur",
            'compact': 'ultra'
        }

        with self.assertRaises(currency_api.Request_Exception) as ex_content:
            conversion_response = currency_api.make_currency_requests(broke_url, params)
        self.assertEqual('Error connecting to currency api', str(ex_content.exception))

    def test_raise_exception_with_wrong_key(self):
        broke_key = '12341j4bhkb1k'
        params = {
            'apiKey': broke_key,
            'q': "USD_eur",
            'compact': 'ultra'
        }

        with self.assertRaises(currency_api.Request_Exception) as ex_content:
            conversion_response = currency_api.make_currency_requests(currency_api.currency_convertor_url, params)
        self.assertEqual("Invalid Free API Key. If you're a premium user, use the api key on https://api. instead of https://free.", str(ex_content.exception))

