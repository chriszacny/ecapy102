import requests


API_KEY = 'QkdHLuiDHSq7ZEDQ7e5GdNpRr3nFAuRb'
QUERY = 'http://terminal2.expedia.com:80/x/hotels?maxhotels=10&location=47.6063889%2C-122.3308333&radius=5km&apikey={}'.format(API_KEY)


class Hotel(object):
    def __init__(self, json_data):
        self.hotel_name = json_data['Name']
        self.hotel_city = json_data['Location']['City']

    def __repr__(self):
        return '{}, {}'.format(self.hotel_name, self.hotel_city)


def get_hotel_json_data():
    return requests.get(QUERY).json()


def main():
    json_data = get_hotel_json_data()
    for json_item in json_data['HotelInfoList']['HotelInfo']:
        hotel = Hotel(json_item)
        print(hotel)


if __name__ == '__main__':
    main()