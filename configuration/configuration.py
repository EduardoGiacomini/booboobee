import os
import logging
from .logger import Logger


class Configuration:
    def __init__(self):
        self.__set_default_configurations()
        self.__setup_logger()

    def __set_default_configurations(self):
        self.logger_level = int(os.getenv('LOG_LEVEL')) if os.getenv('LOG_LEVEL') else logging.DEBUG
        self.weather_api_key = str(os.getenv('WEATHER_API_KEY'))
        self.weather_locale = int(os.getenv('WEATHER_LOCALE'))

    def __setup_logger(self):
        Logger.setup(self.logger_level)
