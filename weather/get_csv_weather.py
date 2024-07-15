import pandas as pd
from api_weather import get_weather_data


cities = ["Miami", "London", "Paris", "Barcelona", "Madrid"]
key = "482ed3291eb0845ec7abf2c7fde2840e"

data_weather = get_weather_data(key = key, *cities)

data_weather.to_csv('weather.csv', index=False)