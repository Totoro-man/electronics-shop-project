from src.item import Item


class Phone(Item):
    """
    Класс для представления Телефона, потомка класса Item.
    """
    def __init__(self, name, price, quantity, number_of_sim: int) -> None:
        """
        Создаем экземпляр класса Item
        добавляем ему свойство number_of_sim
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    """
    Getter|Setter для Item.__number_of_sim
    """
    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_value: int):
        try:
            if not isinstance(new_value, int):
                raise TypeError("TypeError: Phone.number_of_sim must be int")
            if new_value < 1:
                raise ValueError("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
            self.__number_of_sim = new_value
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)



