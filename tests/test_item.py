import pytest
from src.item import Item


class TestItem:

    def test_item_added_to_all(self):
        # Создаем экземпляр товара
        item = Item("Товар 4", 40.0, 4)

        # Проверяем, что созданный товар добавлен в список all
        assert item in Item.all

    def test_calculate_total_price(self):
        # Создаем экземпляр товара
        item = Item("Товар 1", 10.0, 2)

        # Проверяем, что метод calculate_total_price возвращает правильное значение
        assert item.calculate_total_price() == 20.0

    def test_apply_discount(self):
        # Создаем экземпляр товара
        item = Item("Товар 2", 20.0, 3)

        # Применяем скидку
        Item.pay_rate = 0.8
        item.apply_discount()

        # Проверяем, что цена товара изменена в соответствии со скидкой
        assert item.price == 20.0 * Item.pay_rate

    def test_quantity_less_than_zero(self):
        # Попытка создать товар с отрицательным количеством
        with pytest.raises(ValueError):
            Item("Товар 3", 30.0, -1)
