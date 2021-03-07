from configuration import Configuration
from bots import WeatherBot

config = Configuration()
bot = WeatherBot(name='Weather Bot', api_key=config.weather_api_key, locale=config.weather_locale)
bot.get_information()
