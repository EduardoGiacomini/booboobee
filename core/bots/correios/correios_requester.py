import requests

from .correios_adapter import CorreiosAdapter


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
        return self.correios_adapter.to_client(response)

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
