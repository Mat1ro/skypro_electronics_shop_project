from src.phone import Phone


def test_phone_initialization():
    phone = Phone("iPhone", 999.99, 10, 2)
    assert phone.name == "iPhone"
    assert phone.price == 999.99
    assert phone.quantity == 10
    assert phone.number_of_sim == 2


def test_phone_repr():
    phone = Phone("Samsung", 799.99, 5, 1)
    assert repr(phone) == "Phone('Samsung', 799.99, 5, 1)"


def test_number_of_sim_setter_valid():
    phone = Phone("Pixel", 699.99, 8, 3)
    phone.number_of_sim = 4
    assert phone.number_of_sim == 4


def test_number_of_sim_setter_invalid():
    phone = Phone("LG", 499.99, 3, 2)
    try:
        phone.number_of_sim = 0
    except ValueError as e:
        assert str(e) == "Количество физических SIM-карт должно быть целым числом больше нуля."
