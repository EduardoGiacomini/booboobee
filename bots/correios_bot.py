import logging
import requests
from .protocol import BotProtocol


class CorreiosBot(BotProtocol):
    """
        CorreiosBot: bot responsável por dar informações sobre uma encomenda que está sendo transportada pelo correios.
    """
    def __init__(self, name, code):
        super().__init__(name)
        self.code = code
        self.correios_requester = CorreiosRequester(self.code)

    def get_information(self):
        object_tracking = self.correios_requester.get_object_tracking()
        logging.info(f'{self.name} - {object_tracking}')


class CorreiosRequester:
    CORREIOS_HOME_URL = 'https://www2.correios.com.br/sistemas/rastreamento/default.cfm'
    CORREIOS_FORM_TRACKING_URL = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm'
    CORREIOS_RESULT_TRACKING_URL = 'https://www2.correios.com.br/sistemas/rastreamento/resultado.cfm'

    def __init__(self, code):
        self.correios_home_url = self.CORREIOS_HOME_URL
        self.correios_form_tracking_url = self.CORREIOS_FORM_TRACKING_URL
        self.correios_result_tracking_url = self.CORREIOS_RESULT_TRACKING_URL
        self.code = code
        self.session = requests.Session()
        self.correios_adapter = CorreiosAdapter()

    def get_object_tracking(self):
        self.__load_correios_web_site()
        self.__send_object_tracking_form()
        response = self.__get_result_from_object_tracking_form()
        self.correios_adapter.to_client(response)

    def __load_correios_web_site(self):
        self.session.get(self.correios_home_url)

    def __send_object_tracking_form(self):
        form_data = {
            'acao': 'track',
            'objetos': self.code,
            'btnPesq': 'Buscar'
        }
        self.session.post(self.correios_form_tracking_url, data=form_data, allow_redirects=False)

    def __get_result_from_object_tracking_form(self):
        return self.session.get(self.correios_result_tracking_url)


class CorreiosAdapter:
    @staticmethod
    def to_client(response):
        raise NotImplementedError
