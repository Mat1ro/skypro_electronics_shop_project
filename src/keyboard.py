from src.item import Item


class MixinLog:
    def __init__(self, name: int, price: float, quantity: int, language: str) -> None:
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self) -> str:
        return self._language

    @language.setter
    def language(self, new_language: str) -> None:
        self._language = new_language

    def change_lang(self):
        if self.language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"


class Keyboard(MixinLog, Item):
    def __init__(self, name: int, price: float, quantity: int, language: str = "EN"):
        super().__init__(name, price, quantity, language)

