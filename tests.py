# coding: utf-8

import unittest
import customers_invitation as ci


class TestDistanceMethods(unittest.TestCase):
    '''
    Customers data sorted by real distance to Dublin Office
    '''
    __test_customers = [
            {
                'latitude': 53.1302756,
                'user_id': 5,
                'name': 'Nora Dempsey',
                'longitude': -6.2397222,
                'distance': 23.287320663099482
            },
            {
                'latitude': 52.986375,
                'user_id': 12,
                'name': 'Christina McArdle',
                'longitude': -6.043701,
                'distance': 41.7687255008362
            },
            {
                'latitude': 54.1225,
                'user_id': 27,
                'name': 'Enid Gallagher',
                'longitude': -8.143333,
                'distance': 151.5430237149729
            },
            {
                'latitude': 51.999447,
                'user_id': 14,
                'name': 'Helen Cahill',
                'longitude': -9.742744,
                'distance': 278.2067221536596
            },
        ]

    def test_Haversine(self):
        '''
        Apply Haversine formula to calculate distance from each test customer
        to Dublin Office and compare to provided distances
        '''

        for customer in self.__test_customers:
            current_coord = (customer['latitude'], customer['longitude'])
            distance_to_office = ci.calculate_distance(current_coord,
                                                       ci.OFFICE_COORD)
            self.assertEqual(distance_to_office, customer['distance'])

    def test_clients_in_20km_radius_from_office(self):
        max_distance = 20
        expected_customers = 0
        self.__run_test(max_distance, expected_customers)

    def test_clients_in_40km_radius_from_office(self):
        max_distance = 40
        expected_customers = 1
        self.__run_test(max_distance, expected_customers)

    def test_clients_in_100km_radius_from_office(self):
        max_distance = 100
        expected_customers = 2
        self.__run_test(max_distance, expected_customers)

    def test_clients_in_200km_radius_from_office(self):
        max_distance = 200
        expected_customers = 3
        self.__run_test(max_distance, expected_customers)

    def test_clients_in_300km_radius_from_office(self):
        max_distance = 300
        expected_customers = 4
        self.__run_test(max_distance, expected_customers)

    def __run_test(self, max_distance, expected_customers):
        '''
        Helper function to actually run the test according to different
        distances and expected results.

        Since test customers data is sorted by real distance to Dublin Office,
        we can slice this list and compare it to expected result list
        '''

        nearby_customers = ci.get_nearby_customers(self.__test_customers,
                                                   max_distance)
        self.assertEqual(len(nearby_customers), expected_customers)
        self.assertEqual(nearby_customers,
                         self.__test_customers[:expected_customers])


if __name__ == '__main__':
    unittest.main()
