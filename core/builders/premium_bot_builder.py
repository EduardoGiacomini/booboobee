from core.protocol import PremiumBotBuilderProtocol
from core.bots import BotGroup, CorreiosBot, DollarBot, WeatherBot


class PremiumBotBuilder(PremiumBotBuilderProtocol):
    def __init__(self, configuration):
        super().__init__(configuration)
        self.bot_group = BotGroup()

    def build_correios_bot(self):
        self.bot_group.add(CorreiosBot(name='Correios Bot',
                                       code=self.configuration.correios_code))
        return self

    def build_dollar_bot(self):
        self.bot_group.add(DollarBot(name='Dollar Bot'))
        return self

    def build_weather_bot(self):
        self.bot_group.add(WeatherBot(name='Weather Bot',
                                      api_key=self.configuration.weather_api_key,
                                      locale=self.configuration.weather_locale))
        return self

    def build(self):
        return self.bot_group
