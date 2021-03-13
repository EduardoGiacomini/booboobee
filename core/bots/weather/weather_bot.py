import logging
from core.protocol import BotProtocol
from .weather_requester import WeatherRequester


class WeatherBot(BotProtocol):
    """
        WeatherBot: bot responsável por apresentar informações sobre o tempo do dia para o local especificado.
    """
    def __init__(self, name, api_key, locale):
        super().__init__(name)
        self.api_key = api_key
        self.locale = locale
        self.weather_requester = WeatherRequester(self.api_key, self.locale)

    def get_information(self):
        day_weather = self.weather_requester.get_day_weather()
        logging.info(f'{self.name} - {day_weather}')
