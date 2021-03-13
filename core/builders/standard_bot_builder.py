from core.protocol import StandardBotBuilderProtocol
from core.bots import BotGroup, DollarBot


class StandardBotBuilder(StandardBotBuilderProtocol):
    def __init__(self, configuration):
        super().__init__(configuration)
        self.bot_group = BotGroup()

    def build_dollar_bot(self):
        self.bot_group.add(DollarBot(name='Dollar Bot'))
        return self

    def build(self):
        return self.bot_group
