from src.item import Item


class MixinLog:
    def __init__(self, name: int, price: float, quantity: int, language: str) -> None:
        super().__init__(name, price, quantity)
        self.language = language

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"


class Keyboard(MixinLog, Item):
    def __init__(self, name: int, price: float, quantity: int, language: str = "EN"):
        super().__init__(name, price, quantity, language)
