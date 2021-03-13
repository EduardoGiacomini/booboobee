from abc import ABC, abstractmethod


class StandardBotBuilderProtocol(ABC):
    @abstractmethod
    def __init__(self, configuration):
        self.configuration = configuration

    @abstractmethod
    def build_dollar_bot(self):
        pass

    @abstractmethod
    def build(self):
        pass
