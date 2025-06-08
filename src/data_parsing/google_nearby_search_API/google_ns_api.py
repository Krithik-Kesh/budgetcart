import os
from dotenv import load_dotenv
from googlemaps import places
import requests

load_dotenv(verbose=True)
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

api_url = 'https://places.googleapis.com/v1/places:searchNearby'

#Parameters of search and API
header = {
    'Content-Type': 'application/json',
    "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
    "X-Goog-FieldMask": 'places.location,places.displayName,places.shortFormattedAddress,places.websiteUri'
}

#User information for search input
user_search_information = {
    "includedTypes": ["grocery_store"],
    "maxResultCount": 10,
    "locationRestriction": {
        "circle": {
            "center": {
                "latitude": 43.65968025633139,
                "longitude": -79.3980180711644
            },
            "radius": 500.0
        }
    }
}

#response
response = requests.post(api_url, headers=header, json=user_search_information)
data = response.json

