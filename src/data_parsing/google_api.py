import requests

url = "https://places.googleapis.com/v1/places/GyuEmsRBfy61i59si0?fields=addressComponents&key= EMPTY API"

user_loc = {
  "includedTypes": ["grocery_store"],
  "maxResultCount": 10,
  "locationRestriction": {
    "circle": {
      "center": {
        "latitude": 43.646500,
        "longitude": -79.389577},
      "radius": 500.0
    }
  }
}

location_requests = requests.post(url, json = user_loc)

print(location_requests.status_code)