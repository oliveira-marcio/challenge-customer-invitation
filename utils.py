# coding: utf-8

from math import radians, sin, cos, asin, sqrt
import json


def calculate_distance(p1, p2):
    '''
    This method uses Haversine formula to calculate smallest distance between
    2 points on Earth surface.

    https://en.wikipedia.org/wiki/Haversine_formula

    hav = sin(delta_lat/2) * sin(delta_lat/2) +
          cos(lat1) * cos(lat2) *
          sin(delta_lng/2) * sin(delta_lng/2)

    where:

    lat1 = first point latitude (in radius)
    lat1 = second point latitude (in radius)
    delta_lat = difference between latitudes (in radians)
    delta_lng = difference between longitudes (in radians)

    So distance between 2 points should be:

    d = 2 * R * arcsin(sqrt(hav))

    where:

    R = Earth radius (in meters)
    hav = Haversine value of the central angle between 2 points

    The method returns distance in quilometers

    '''

    R = 6371e3
    lat1 = radians(p1[0])
    lat2 = radians(p2[0])
    delta_lat = radians(p2[0] - p1[0])
    delta_lng = radians(p2[1] - p1[1])

    hav = sin(delta_lat/2) * sin(delta_lat/2) + \
        cos(lat1) * cos(lat2) * \
        sin(delta_lng/2) * sin(delta_lng/2)

    return 2*R*asin(sqrt(hav))/1000


def get_customers(filename):
    '''
    Read customers file and return all data as a list of Python Dictionaries.
    In case of error reading the file, an empty list will be returned.
    '''
    customers = []

    try:
        with open(filename) as file:
            for line in file:
                current_json = json.loads(line)
                customers.append(
                    {
                        'latitude': float(current_json['latitude']),
                        'user_id': int(current_json['user_id']),
                        'name': current_json['name'],
                        'longitude': float(current_json['longitude'])
                    }
                )

    except IOError as err:
        filename = ""
        print("I/O error: {}".format(err))

    return customers


def write_invitation_list(filename, customers, max_distance):
    '''
    Method to output invitation list and save it in a text file
    '''

    try:
        with open(filename, 'w') as file:
            line = 'Customers in %s km radius from Dublin Office\n%s' \
                % (max_distance, ('-' * 60))
            print(line)
            file.write(line + '\n')

            if len(customers):
                for customer in customers:
                    line = '%02d) %s' % (customer['user_id'],
                                         customer['name'])
                    print(line)
                    file.write(line + '\n')
                line = '\n%s customers found.' % len(customers)
                print(line)
                file.write(line)
            else:
                line = 'No customers found.'
                print(line)
                file.write(line)

        print('\nArquivo "%s" gravado com sucesso!' % filename)

    except IOError as err:
        print("Erro de I/O: {}".format(err))
