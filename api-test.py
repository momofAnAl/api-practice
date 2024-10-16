import os
import time
from dotenv import load_dotenv
import requests

load_dotenv()

PATH = "https://www.alphavantage.co/query?"

API_KEY = os.getenv("LOCATIONIQ_API_KEY")

SEVEN_WONDERS = ["Great Wall of China", "Christ the Redeemer", \
   "Machu Picchu", "Petra", "Chichen Itza", "Colosseum", "Taj Mahal"]

def get_location_data(wonder_name):
    query_params = {
        "key": API_KEY,
        "q": wonder_name,
        "format": "json"
    }
    
    response = requests.get(PATH, params=query_params)
    time.sleep(.5)
    return response.json()

for wonder in SEVEN_WONDERS:
    if wonder == "Petra":
        location_data = get_location_data(wonder)
        for location in location_data:
            print(f"The lat and lon of {wonder} is {location["lat"]}, {location["lon"]}")
            print(f"The display name of {wonder} is {location["display_name"]}")
            print(f"{wonder} is a {location["type"]} {location["class"]}")
            time.sleep(.5)
            print("\n")






















# SEVEN_WONDERS = ["Great Wall of China", "Christ the Redeemer", \
#    "Machu Picchu", "Petra", "Chichen Itza", "Colosseum", "Taj Mahal"]

# def get_location_data(wonder_name):
#     query_params = {
#         "key": API_KEY,
#         "q": wonder_name,
#         "format": "json"
#     }
#     response = requests.get(PATH, params=query_params)
#     time.sleep(.5)
#     return response.json()

# for wonder in SEVEN_WONDERS:
#     if wonder == "Petra":
#         location_data = get_location_data(wonder)
#         for location in location_data:
#             print(f"The lat and lon of {wonder} is {location["lat"]}, {location["lon"]}")
#             print(f"The display name of {wonder} is {location["display_name"]}")
#             print(f"{wonder} is a {location["type"]} {location["class"]}")
#             time.sleep(1)
#             print("\n")

