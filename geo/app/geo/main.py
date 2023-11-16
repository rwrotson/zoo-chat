from sys import argv
from geopy.geocoders import Nominatim
from geopy.location import Location


def get_location(place: str) -> Location:
    place = ' '.join(place.strip().split('_'))
    geolocator = Nominatim(user_agent='Zoo')
    location = geolocator.geocode(place)
    print('location:', location)
    return location.latitude, location.longitude


if __name__=='__main__':
    place = argv[1]
    get_location(place)
