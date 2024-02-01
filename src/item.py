import csv

from src.exceptions.instantiateCSVError import InstantiateCSVError


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price, quantity) -> None:
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
        try:
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        name, price, quantity = row["name"], row['price'], row['quantity']
                    except Exception:
                        raise InstantiateCSVError(path)
                    else:
                        cls(name, price, quantity)
        except FileNotFoundError:
            print(f"No {path} file or directory")

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price = self.price * Item.pay_rate

    @staticmethod
    def string_to_number(string: str):
        return int(float(string))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self._name = new_name
        else:
            self._name = new_name[:10]
