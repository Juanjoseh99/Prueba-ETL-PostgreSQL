import pandas as pd
import requests


def get_weather_data(*cities, key):
    
    units = "metric"  # Celsius

    data_weather = []

    for city in cities: 
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units={units}'
        response = requests.get(URL)
        if response.status_code == 200:
            info = response.json()
            data_weather.append({
                'city': info['name'],
                'temperature': info['main']['temp'],
                'humidity': info['main']['humidity'],
                'weather': info['weather'][0]['description']
            })

    df_data_weather = pd.DataFrame(data_weather)

    return df_data_weather

