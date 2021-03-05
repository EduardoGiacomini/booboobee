import requests
from .protocol import BotProtocol


class WeatherBot(BotProtocol):
    def __init__(self, name, api_key, locale):
        super().__init__(name)
        self.api_key = api_key
        self.locale = locale
        self.weather_requester = WeatherRequester(self.api_key, self.locale)

    def get_information(self):
        weather_information = self.weather_requester.get_day_weather()
        print(f'{self.name} -', weather_information)


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


class WeatherAdapter:
    @staticmethod
    def to_client(response):
        prevision_day = response['data'][0]['date_br']
        weather_resume = response['data'][0]['text_icon']['text']['phrase']['reduced']
        min_temperature = response['data'][0]['temperature']['min']
        max_temperature = response['data'][0]['temperature']['max']
        rain_probability = response['data'][0]['rain']['probability']
        rain_precipitation = response['data'][0]['rain']['precipitation']
        adapted_response = f'Previsão do dia {prevision_day}: {weather_resume} Temperatura entre {min_temperature:.0f}°C' \
                           f' e {max_temperature:.0f}°C. Probabilidade de {rain_probability:.0f}% para chuvas de até ' \
                           f'{rain_precipitation:.0f} mm.'
        return adapted_response
