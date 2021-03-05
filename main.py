from bots import WeatherBot

bot = WeatherBot(name='Weather Bot', api_key='secret_key', locale='secret_locale')
bot.get_information()
