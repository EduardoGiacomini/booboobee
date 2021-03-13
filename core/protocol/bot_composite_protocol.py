from abc import ABC, abstractmethod


class BotCompositeProtocol(ABC):
    @abstractmethod
    def __init__(self):
        self.bots = []

    @abstractmethod
    def get_information(self):
        pass
