from core.protocol import BotCompositeProtocol


class BotGroup(BotCompositeProtocol):
    def __init__(self):
        super().__init__()

    def add(self, bot):
        self.bots.append(bot)

    def get_information(self):
        bot_information = ''
        for bot in self.bots:
            bot_information += f'--- {bot.name} ---\n{bot.get_information()}\n'
        return bot_information
