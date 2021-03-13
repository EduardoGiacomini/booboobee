from abc import ABC, abstractmethod


class BotProtocol(ABC):
    @abstractmethod
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_information(self) -> str:
        pass
