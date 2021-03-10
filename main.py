from configuration import Configuration
from bots import WeatherBot, DollarBot, CorreiosBot

config = Configuration()
weather_bot = WeatherBot(name='Weather Bot', api_key=config.weather_api_key, locale=config.weather_locale)
dollar_bot = DollarBot(name='Dollar Bot')
correios_bot = CorreiosBot(name='Correios Bot', code='')

weather_bot.get_information()
dollar_bot.get_information()
correios_bot.get_information()
