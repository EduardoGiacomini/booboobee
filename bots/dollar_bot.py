import logging
import requests
from .protocol import BotProtocol
from .utils import CurrencyUtils, DatetimeUtils


class DollarBot(BotProtocol):
    """
        DollarBor: bot responsável por dar informações sobre a cotação do dólar do dia.
    """
    def __init__(self, name):
        super().__init__(name)
        self.dollar_requester = DollarRequester()

    def get_information(self):
        dollar_information = self.dollar_requester.get_day_dollar_cotation()
        logging.info(f'{self.name} - {dollar_information}')


class DollarRequester:
    DOLLAR_API_URL = 'https://economia.awesomeapi.com.br'

    def __init__(self):
        self.dollar_api_url = self.DOLLAR_API_URL
        self.dollar_adapter = DollarAdapter()

    def get_day_dollar_cotation(self):
        url = f'{self.dollar_api_url}/all/USD-BRL'
        response = requests.get(url)
        return self.dollar_adapter.to_client(response.json())


class DollarAdapter:
    @staticmethod
    def to_client(response):
        cotation_day, cotation_hour = response['USD']['create_date'].split(' ')
        formatted_cotation_day = DatetimeUtils.to_brazilian_format(cotation_day)
        cotation_value = response['USD']['high']
        formatted_cotation_value = CurrencyUtils.to_brazilian_format(cotation_value)
        adapted_response = f'Cotação do dólar comercial do dia {formatted_cotation_day}: R${formatted_cotation_value}.'
        return adapted_response
