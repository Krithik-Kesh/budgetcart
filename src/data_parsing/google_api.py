import requests

url = "https://places.googleapis.com/v1/places/GyuEmsRBfy61i59si0?fields=addressComponents&key=AIzaSyD1q9Kb6mudmD4FvEJ7f1v5J9r7BG7dv3E"

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