import os
import time
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# API settings
PATH = "https://us1.locationiq.com/v1/search.php"
API_KEY = os.getenv("LOCATIONIQ_API_KEY")

SEVEN_WONDERS = [
    "Great Wall of China", "Christ the Redeemer", "Machu Picchu",
    "Petra", "Chichen Itza", "Colosseum", "Taj Mahal"
]

wonders_data = {}

def get_location_data(wonder_name):
    """Fetch location data from API for a given wonder."""
    query_params = {
        "key": API_KEY,
        "q": wonder_name,
        "format": "json"
    }
    
    response = requests.get(PATH, params=query_params)
    
    if response.status_code != 200:
        print(f"Error fetching data for {wonder_name}: {response.status_code}")
        return None 

    time.sleep(0.5) 
    return response.json()

def extract_location_data(wonder, location_data):
    """Extract latitude and longitude from API response and store in wonders_data."""
    if isinstance(location_data, list) and len(location_data) > 0:
        location = location_data[0]  # Get first location result
        wonders_data[wonder] = {
            "latitude": location.get("lat", "N/A"),
            "longitude": location.get("lon", "N/A")
        }
    else:
        print(f"No valid location data found for {wonder}.")
        wonders_data[wonder] = {"latitude": "N/A", "longitude": "N/A"}

def fetch_all_wonders():
    """Fetch locations for all Seven Wonders and store in a dictionary."""
    for wonder in SEVEN_WONDERS:
        location_data = get_location_data(wonder)
        extract_location_data(wonder, location_data)
        time.sleep(0.5)  # Avoid hitting API rate limits

def display_results():
    """Print out the results from wonders_data."""
    print("\n### Seven Wonders Locations ###\n")
    for wonder, coords in wonders_data.items():
        print(f"{wonder}: Latitude {coords['latitude']}, Longitude {coords['longitude']}\n")

fetch_all_wonders()
display_results()

