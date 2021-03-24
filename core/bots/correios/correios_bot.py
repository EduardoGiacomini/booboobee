from core.protocol import BotProtocol
from .correios_requester import CorreiosRequester


class CorreiosBot(BotProtocol):
    """
        CorreiosBot: bot responsável por apresentar informações sobre uma encomenda transportada pelo correios.
    """
    def __init__(self, name, code):
        super().__init__(name)
        self.code = code
        self.correios_requester = CorreiosRequester(self.code)

    def get_information(self):
        return self.correios_requester.get_object_tracking()
