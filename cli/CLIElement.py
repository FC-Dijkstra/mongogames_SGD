from abc import ABC, abstractmethod

class CLIElement:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def handleInput(self):
        pass