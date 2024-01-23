from src.keyboard import Keyboard


class TestKeyboard:

    def test_keyboard(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert kb.quantity == 5
        assert kb.language == "EN"
        assert kb.name == "Dark Project KD87A"
        assert kb.price == 9600

    def test_change_language(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert kb.language == "EN"

        kb.change_lang()
        assert kb.language == "RU"

        kb.change_lang()
        assert kb.language == "EN"

    def test_language_set(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        try:
            kb.language = "RU"
        except AttributeError as e:
            assert str(e) == "property 'language' of 'Keyboard' object has no setter"
