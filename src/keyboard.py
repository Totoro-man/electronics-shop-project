from src.item import Item
from src.itemsmixin import ItemsMixIn


class Keyboard(ItemsMixIn, Item):
    """
    Класс для представления Клавиатуры, потомка класса Item.
    """
    """
    Getter|Setter для Item.__name
    """
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise TypeError("Item.name must be str")

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity}, {self.language})"
