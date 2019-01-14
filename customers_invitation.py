# coding: utf-8


from utils import get_customers, calculate_distance, write_invitation_list

OFFICE_COORD = (53.339428, -6.257664)


def get_nearby_customers(customers, max_distance):
    '''
    Get a list of customers inside radius provided from Dublin Office
    '''

    nearby_customers = []

    for customer in customers:
        current_coord = (customer['latitude'], customer['longitude'])
        if calculate_distance(current_coord, OFFICE_COORD) <= max_distance:
            nearby_customers.append(customer)

    return nearby_customers


if __name__ == '__main__':

    all_customers = get_customers('customers.txt')
    MAX_DISTANCE = 100

    nearby_customers = get_nearby_customers(all_customers, MAX_DISTANCE)
    nearby_customers = sorted(nearby_customers, key=lambda k: k['user_id'])

    write_invitation_list('invitation.txt', nearby_customers, MAX_DISTANCE)
