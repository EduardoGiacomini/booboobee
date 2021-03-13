import requests
from .weather_adapter import WeatherAdapter


class WeatherRequester:
    WEATHER_API_URL = 'http://apiadvisor.climatempo.com.br/api/v1'

    def __init__(self, api_key, locale):
        self.weather_api_url = self.WEATHER_API_URL
        self.api_key = api_key
        self.locale = locale
        self.weather_adapter = WeatherAdapter()

    def get_day_weather(self):
        url = f'{self.weather_api_url}/forecast/locale/{self.locale}/days/15?token={self.api_key}'
        response = requests.get(url)
        return self.weather_adapter.to_client(response.json())
