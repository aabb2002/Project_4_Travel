##TODO
# testing for APIs


from unittest import TestCase 
from unittest.mock import patch
import currency_api
import weather_api 

# python3 -m unittest Tests/test_geocoder_api.py
class TestAPI(TestCase):

    # happy path
    def test_generate_geocode_parameters(self):
        params = weather_api.generate_request_params_for_location('Minneapolis', 'MN')
        self.assertEqual(params, {
            'q': 'Minneapolis,MN',
            'appid': weather_api.weather_key,
            'limit': 1
        })

    @patch('weather_api.make_geocode_request', return_value=[{ 'name': 'minneapolis', 'lat': 45, 'lon': -93} ])
    def test_weather_response(self, mock_response):
        params = weather_api.get_weather_forecast('us', 'Minneapolis')
        self.assertEqual(params, ['On 2022-03-23: it should be 34.84F. Description: snow '])


    # todo unhappy paths - missing data, weird data  etc. 
    def test_generate_geocode_parameters_missing_data(self):
        params = weather_api.generate_request_params_for_location(None, 'MN')
        self.assertEqual(params, None)


    @patch('weather_api.make_geocode_request', return_value=[{ 'name': 'minneapolis', 'lat': 45, 'lon': -93} ])
    def test_convert_location(self, mock_response):
        lat, lon = weather_api.convert_location_to_lat_and_lon('Minneapolis', 'USA')
        self.assertEqual(45, lat)
        self.assertEqual(-93, lon)

    # @patch('weather_api.make_geocode_request', return_value=[{ 'name': 'minneapolis', 'lat': 45, 'lon': -93} ])
    # def test_raise_exception_with_wrong_weather_url(self, mock_response):
    #     broke_url = 'www.notweatherapi.gov'
    #     params = {
    #         'lat': 45, 
    #         'lon': -93, 
    #         'units': 'imperial', 
    #         'appid': weather_api.weather_key, 
    #         'exclude': 'minutely, hourly, alerts',
    #         'units': 'imperial'
    #     }

    #     with self.assertRaises(currency_api.Request_Exception) as ex_content:
    #         weather_response = weather_api.get_weather_forecast('minneapolis', 'us')
    #     self.assertEqual('Error connecting to weather api', str(ex_content.exception))



        