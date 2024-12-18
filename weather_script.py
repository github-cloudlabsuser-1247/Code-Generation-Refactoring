import requests

# Fetch weather data from OpenWeatherMap API
def fetch_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
api_key = '53771ccf740edc3c757be8c6b5bcdeb2'
city = 'London'
weather_data = fetch_weather(api_key, city)
if weather_data:
    print(weather_data)
else:
    print("Failed to fetch weather data")

