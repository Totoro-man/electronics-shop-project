from src.phone import Phone
import pytest


def test_phone_init(test_item):
    assert test_item[3].name == "iPhone 14"
    assert test_item[3].number_of_sim == 2


def test__repr__(test_item):
    assert repr(test_item[3]) == "Phone('iPhone 14', 120000, 5, 2)"


def test_items_addition(test_item):
    assert test_item[0] + test_item[1] == 3
    assert test_item[0] + test_item[3] == 6
    with pytest.raises(TypeError, match=".* Item or Phone"):
        test_item[0] + 5
