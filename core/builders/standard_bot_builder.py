from core.protocol import StandardBotBuilderProtocol
from core.bots import BotGroup, DollarBot, WeatherBot


class StandardBotBuilder(StandardBotBuilderProtocol):
    def __init__(self, configuration):
        super().__init__(configuration)
        self.bot_group = BotGroup()

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

