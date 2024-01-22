"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


TEST_ITEM_1 = Item("Левый носок", 1000, 1)
TEST_ITEM_2 = Item("Правый носок", 2000, 2)
TEST_ITEM_3 = Item("Резинка от трусов", 3000, 3)


@pytest.fixture
def test_item():
    return TEST_ITEM_1, TEST_ITEM_2, TEST_ITEM_3


def test_item_init():
    assert len(Item.all) == 3
    test_item_4 = Item("Парик", 4000, 4)
    assert test_item_4.name == "Парик"
    assert test_item_4.price == 4000
    assert test_item_4.quantity == 4
    assert len(Item.all) == 4


def test_calculate_total_price(test_item):
    assert Item.calculate_total_price(test_item[0]) == 1000
    assert Item.calculate_total_price(test_item[1]) == 4000
    assert Item.calculate_total_price(test_item[2]) == 9000


def test_apply_discount():
    Item.pay_rate = 1
    TEST_ITEM_1.apply_discount()
    assert TEST_ITEM_1.price == 1000

    Item.pay_rate = 0.1
    TEST_ITEM_1.apply_discount()
    assert TEST_ITEM_1.price == 100

    Item.pay_rate = 2
    TEST_ITEM_1.apply_discount()
    assert  TEST_ITEM_1.price == 200
