# 2. Use web search to find some API to get weather data. Use that to get your region’s weather data every 30 minute.

# Write a function named weather_data() and write your code inside this function.

from time import sleep
import requests
import json


api_key='https://api.openweathermap.org/data/2.5/weather?q=chittagong&appid=4b5f5c378962441c1c0063e2bb400c5c'

while True:
    response_API = requests.get(api_key)
    data = response_API.text
    parse_Data = json.loads(data)
    print(parse_Data)
    sleep(1800)

