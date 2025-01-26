from datetime import datetime
import requests

class WeatherSkill:
    def __init__(self, config):
        self.api_key = config.get('apis.weather_key')
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.base_url, params=params, timeout=5)
            data = response.json()
            
            if response.status_code == 200:
                temp = round(data['main']['temp'])
                condition = data['weather'][0]['description']
                humidity = data['main']['humidity']
                return f"The current weather in {city} is {temp}°C with {condition}. Humidity is {humidity}%"
            return "I'm having trouble getting the weather information right now."
            
        except Exception as e:
            return "I couldn't fetch the weather data at the moment. Please try again."


