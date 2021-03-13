import requests
from .dollar_adapter import DollarAdapter


class DollarRequester:
    DOLLAR_API_URL = 'https://economia.awesomeapi.com.br'

    def __init__(self):
        self.dollar_api_url = self.DOLLAR_API_URL
        self.dollar_adapter = DollarAdapter()

    def get_day_dollar_cotation(self):
        url = f'{self.dollar_api_url}/all/USD-BRL'
        response = requests.get(url)
        return self.dollar_adapter.to_client(response.json())
