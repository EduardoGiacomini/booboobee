from configuration import configuration
from core import PremiumBotBuilder


class Main:
    @staticmethod
    def run():
        premium_bots = PremiumBotBuilder(configuration).build_dollar_bot().build_weather_bot().build()
        print(premium_bots.get_information())


Main.run()
