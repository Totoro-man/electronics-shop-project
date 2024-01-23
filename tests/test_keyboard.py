import pytest

from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_init():
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"


def test_name():
    kb.name = "Bla-bla-bla"
    assert kb.name == "Bla-bla-bla"

    with pytest.raises(TypeError):
        kb.name = 1