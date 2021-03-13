from core.protocol import BotCompositeProtocol


class BotComposite(BotCompositeProtocol):
    def __init__(self):
        self.bots = []

    def add(self, bot):
        self.bots.append(bot)

    def get_information(self):
        for bot in self.bots:
            bot.get_information()
