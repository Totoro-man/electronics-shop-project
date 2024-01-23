import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """А еще подрезаем имя до 10 знаков"""
        if isinstance(new_name, str):
            self.__name = new_name[:10]
        else:
            raise TypeError("Item.name must be str")

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if isinstance(new_price, float | int):
            self.__price = new_price
        else:
            raise TypeError("Item.price must be float or int")

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        if isinstance(new_quantity, int):
            self.__quantity = new_quantity
        else:
            raise TypeError("Item.quantity must be int")

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> None:
        with open(file_path, newline='') as csvfile:
            item_list = csv.DictReader(csvfile)
            for i in item_list:
                Item(i.get("name"), Item.string_to_number(i.get("price")), Item.string_to_number(i.get("quantity")))

    @classmethod
    def string_to_number(cls, number_sting: str) -> int:
        return int(float(number_sting))

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("adding variable must be Item or Phone")