from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def test_item():
    Item.all.clear()
    t1 = Item("Левый носок", 1000, 1)
    t2 = Item("Правый носок", 2000, 2)
    t3 = Item("Резинка от трусов", 3000, 3)
    p1 = Phone("iPhone 14", 120_000, 5, 2)
    return t1, t2, t3, p1
