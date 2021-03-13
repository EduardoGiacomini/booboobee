import logging

from core.protocol import BotProtocol
from .dollar_requester import DollarRequester


class DollarBot(BotProtocol):
    """
        DollarBor: bot responsável por apresentar informações sobre a cotação do dólar do dia.
    """
    def __init__(self, name):
        super().__init__(name)
        self.dollar_requester = DollarRequester()

    def get_information(self):
        day_dollar_cotation = self.dollar_requester.get_day_dollar_cotation()
        logging.info(f'{self.name} - {day_dollar_cotation}')
