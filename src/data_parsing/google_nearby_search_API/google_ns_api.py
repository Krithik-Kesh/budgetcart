import googlemaps
import os
from dotenv import load_dotenv

MILES_TO_METRES = 1,609.344

load_dotenv()
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def turn_miles_to_meters(miles):
  try:
    return miles * MILES_TO_METRES
  except ValueError as val:
    print(f"{val} not a valid input.")

#API STUFF
ME = googlemaps.Client(GOOGLE_MAPS_API_KEY)

#USER LOCATION INITIALIZATION AND GOOGLE API STORE FINDER
user_location = (43.647068, -79.390436) #Generic location
search = 'grocery_store'
distance = turn_miles_to_meters(15)
list_of_stores = []

c
response = ME.places_nearby(
  location = user_location,
  keyword = search,
  name = 'grocery stores',
  radius = distance
)

list_of_stores.extend(response.get('results'))
file = open('../results.txt', 'w')
file.writelines(str(list_of_stores))
