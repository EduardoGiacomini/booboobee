from configuration import Configuration
from bots import CorreiosBot

config = Configuration()
correios_bot = CorreiosBot(name='Correios Bot', code='')

correios_bot.get_information()
