"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def test_item():
    Item.all.clear()
    t1 = Item("Левый носок", 1000, 1)
    t2 = Item("Правый носок", 2000, 2)
    t3 = Item("Резинка от трусов", 3000, 3)
    return t1, t2, t3


def test_item_init(test_item):
    assert len(Item.all) == 3
    test_item_4 = Item("Фига в носке", 4000, 4)
    assert test_item_4.name == "Фига в нос"
    assert test_item_4.price == 4000
    assert test_item_4.quantity == 4
    assert len(Item.all) == 4


with pytest.raises(TypeError, match=".* str"):
    Item(1, 1, 3)
with pytest.raises(TypeError, match=".* float .*"):
    Item("1", "1", 3)
with pytest.raises(TypeError, match=".* int"):
    Item("1", 1, 3.0)


def test_calculate_total_price(test_item):
    assert Item.calculate_total_price(test_item[0]) == 1000
    assert Item.calculate_total_price(test_item[1]) == 4000
    assert Item.calculate_total_price(test_item[2]) == 9000


def test_apply_discount(test_item):
    Item.pay_rate = 1
    test_item[0].apply_discount()
    assert test_item[0].price == 1000

    Item.pay_rate = 0.1
    test_item[0].apply_discount()
    assert test_item[0].price == 100

    Item.pay_rate = 2
    test_item[0].apply_discount()
    assert test_item[0].price == 200


def test_instantiate_from_csv():
    Item.all.clear()
    Item.instantiate_from_csv("src/items.csv")
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[1].price == 1000
    assert Item.all[2].quantity == 5


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test__str__(test_item):
    assert str(test_item[0]) == "Левый носок"[:10]
    assert str(test_item[1]) == "Правый носок"[:10]
    assert str(test_item[2]) == "Резинка от трусов"[:10]


def test__repr__(test_item):
    assert repr(test_item[0]) == "Item('Левый носо', 1000, 1)"
    assert repr(test_item[1]) == "Item('Правый нос', 2000, 2)"
    assert repr(test_item[2]) == "Item('Резинка от', 3000, 3)"
