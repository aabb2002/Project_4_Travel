##TODO
# testing for APIs


from unittest import TestCase 
from unittest.mock import patch
import travel_APIs 

# python3 -m unittest Tests.test_travel_APIs
class TestAPI(TestCase):

    # happy path
    def test_generate_geocode_parameters(self):
        params = travel_APIs.generate_request_params_for_location('Minneapolis', 'MN')
        self.assertEqual(params, {
            'q': 'Minneapolis,MN',
            'appid': travel_APIs.weather_key,
            'limit': 1
        })


    # todo unhappy paths - missing data, weird data  etc. 
    def test_generate_geocode_parameters_missing_data(self):
        params = travel_APIs.generate_request_params_for_location(None, 'MN')
        self.assertEqual(params, None)


    @patch('travel_APIs.make_geocode_request', return_value=[{ 'name': 'minneapolis', 'lat': 45, 'lon': -93} ])
    def test_convert_location(self, mock_response):
        lat, lon = travel_APIs.convert_location_to_lat_and_lon('Minneapolis', 'USA')
        self.assertEqual(45, lat)
        self.assertEqual(-93, lon)