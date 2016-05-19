__author__ = 'czacny'


def get_mock_hotel_data():
    data = []
    hilton_hotel = {}
    hilton_hotel['hotel_id'] = 12345
    hilton_hotel['amenities'] = [WheelchairAccessibleBehavior, FitnessFacilityBehavior, PoolBehavior]
    hilton_hotel['amenity_data'] = {'weights_type': 'free', 'pool_type': 'indoors'}

    data.append(hilton_hotel)

    travel_lodge_hotel = {}
    travel_lodge_hotel['hotel_id'] = 987875
    travel_lodge_hotel['amenities'] = [WheelchairAccessibleBehavior, FitnessFacilityBehavior]
    travel_lodge_hotel['amenity_data'] = {'weights_type': 'barbell'}

    data.append(travel_lodge_hotel)
    return data


def WheelchairAccessibleBehavior(**kwargs):
    print('This hotel has wheelchair accessible facilities.')


def FitnessFacilityBehavior(**kwargs):
    print('This hotel has a fitness facility. It has {} weights.'.format(kwargs['weights_type']))


def PoolBehavior(**kwargs):
    print('This hotel has a pool. It is {}.'.format(kwargs['pool_type']))


def analyze_hotel_data(hotel_data):
    for raw_data in hotel_data:
        print('')
        print('Analyzing hotel {}'.format(raw_data['hotel_id']))
        for amenity_func in raw_data['amenities']:
            amenity_func(**raw_data['amenity_data'])


def main():
    hotel_data = get_mock_hotel_data()
    analyze_hotel_data(hotel_data)


if __name__ == '__main__':
    main()