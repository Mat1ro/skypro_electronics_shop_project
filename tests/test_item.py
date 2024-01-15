import pytest
from src.item import Item
from src.phone import Phone


class TestItem:

    def test_item_added_to_all(self):
        """
        Тест проверяет, что созданный товар добавлен в список 'all' класса Item.
        """
        item = Item("Товар 4", 40.0, 4)

        assert item in Item.all

    def test_calculate_total_price(self):
        """
        Тест проверяет, что метод calculate_total_price возвращает правильное значение.
        """
        item = Item("Товар 1", 10.0, 2)

        assert item.calculate_total_price() == 20.0

    def test_apply_discount(self):
        """
        Тест проверяет, что метод apply_discount правильно применяет скидку к товару.
        """
        item = Item("Товар 2", 20.0, 3)

        Item.pay_rate = 0.8
        item.apply_discount()

        assert item.price == 20.0 * Item.pay_rate

    def test_quantity_less_than_zero(self):
        """
        Тест проверяет, что создание товара с отрицательным количеством вызывает ValueError.
        """
        with pytest.raises(ValueError):
            Item("Товар 3", 30.0, -1)

    def test_string_to_number(self):
        """
        Тест проверяет, что метод string_to_number корректно преобразует строку в число.
        """
        assert Item.string_to_number('10.5') == 10
        assert Item.string_to_number('20.7') == 20
        assert Item.string_to_number('5.0') == 5

    def test_instantiate_from_csv(self):
        """
        Тест проверяет, что метод instantiate_from_csv корректно создает экземпляры товаров из CSV-файла.
        """
        Item.instantiate_from_csv("./src/items.csv")
        assert len(Item.all) == 8

    def test_add_items_and_phones(self):
        item = Item("Товар 4", 40.0, 4)
        phone = Phone("Товар 4", 40.0, 4, 2)
        item2 = Item("Товар 4", 40.0, 2)
        phone2 = Phone("Товар 4", 40.0, 7, 2)
        assert item + item2 == 6
        assert phone + phone2 == 11
