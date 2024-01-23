import csv


class Item:
    """
    Класс для представления товара в магазине.

    Attributes:
        pay_rate (float): Ставка оплаты для товара (по умолчанию 1.0).
        all (list): Список всех созданных экземпляров товаров.
    """

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Инициализирует экземпляр класса Item.

        Args:
            name (str): Название товара.
            price (float): Цена товара.
            quantity (int): Количество товара.

        Raises:
            ValueError: Если цена или количество отрицательны.
        """
        if Item.string_to_number(price) < 0 or Item.string_to_number(quantity) < 0:
            raise ValueError
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self._name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return other.quantity + self.quantity

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Создает экземпляры товаров из CSV-файла и добавляет их в список.

        Args:
            path (str): Путь к CSV-файлу.
        """
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        Returns:
            float: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @staticmethod
    def string_to_number(string: str):
        """
        Преобразует строку в число.

        Args:
            string (str): Строка, представляющая число.

        Returns:
            int: Преобразованное целое число.
        """
        return int(float(string))

    @property
    def name(self):
        """
        Получает название товара.

        Returns:
            str: Название товара.
        """
        return self._name

    @name.setter
    def name(self, new_name):
        """
        Устанавливает название товара.

        Args:
            new_name (str): Новое название товара (не более 10 символов).
        """
        if len(new_name) <= 10:
            self._name = new_name
        else:
            self._name = new_name[:10]
