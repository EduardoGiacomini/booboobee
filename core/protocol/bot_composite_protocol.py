from abc import ABC, abstractmethod


class BotCompositeProtocol(ABC):
    @abstractmethod
    def get_information(self):
        pass
