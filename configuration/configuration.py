import os
import logging
from dotenv import load_dotenv

from .logger import Logger


class Configuration:
    def __init__(self):
        self.__set_default_configurations()
        self.__setup_logger()

    def __set_default_configurations(self):
        load_dotenv()
        self.logger_level = int(os.getenv('LOGGER_LEVEL')) if os.getenv('LOGGER_LEVEL') else logging.DEBUG
        self.correios_code = os.getenv('CORREIOS_CODE')
        self.weather_api_key = os.getenv('WEATHER_API_KEY')
        self.weather_locale = os.getenv('WEATHER_LOCALE')

    def __setup_logger(self):
        Logger.setup(self.logger_level)


configuration = Configuration()
