from configuration import Configuration
from bots import WeatherBot, DollarBot

config = Configuration()
weather_bot = WeatherBot(name='Weather Bot', api_key=config.weather_api_key, locale=config.weather_locale)
dollar_bot = DollarBot(name='Dollar Bot')

weather_bot.get_information()
dollar_bot.get_information()
