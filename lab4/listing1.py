from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
my_address ='Krakow, Marii Konopnickiej 26'
geolocator = Nominatim(user_agent='rs_123457891000098')
try:
    location = geolocator.geocode(my_address)
    print(location.latitude, location.longitude)
except GeocoderTimedOut as e:
    print("Error: geocode failed on input %s with message %s"%(my_address, e.message))