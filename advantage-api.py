import os
import time
from dotenv import load_dotenv
import requests

load_dotenv()

PATH = "https://www.alphavantage.co/query?"

API_KEY = os.getenv("ADVANTAGE_API_KEY")

query_params = {
    "apikey": API_KEY,
    "function": "INFLATION"
}
response = requests.get(PATH, params=query_params)
time.sleep(.5)
# print(response.json())

inflation_datas = response.json()

name = inflation_datas['name']
interval = inflation_datas['interval']
print(f"Name = {name}, Interval: {interval}")

for data in inflation_datas['data']:
    time.sleep(.5)
    print(f"Date: {data['date']}, Value: {data['value']}")