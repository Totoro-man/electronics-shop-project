import csv
import os

from src.csverrors import InstantiateCSVError


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

    """
    Getter|Setter для Item.__name
    """
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        try:
            if not isinstance(new_name, str):
                raise TypeError("Item.name must be str")
            """А еще подрезаем имя до 10 знаков"""
            self.__name = new_name[:10]
        except TypeError as te:
            print(te)

    """
    Getter|Setter для Item.__price
    """
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        try:
            if not isinstance(new_price, float | int):
                raise TypeError("Item.price must be float or int")
            self.__price = new_price
        except TypeError as te:
            print(te)

    """
    Getter|Setter для Item.__quantity
    """
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        try:
            if not isinstance(new_quantity, int):
                raise TypeError("Item.quantity must be int")
            self.__quantity = new_quantity
        except TypeError as te:
            print(te)

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> None:
        """
        Преобразование данных из файла в список экземпляров класса Item
        :param file_path: путь к файлу данных
        """
        Item.all.clear()
        file_path = Item.normalize_path(file_path)
        try:
            with open(file_path, newline='') as csvfile:
                item_list = csv.DictReader(csvfile)
                item_list = list(item_list)
                if len(item_list[0]) == 3:
                    for i in item_list:
                        Item(i.get("name"), Item.string_to_number(i.get("price")),
                             Item.string_to_number(i.get("quantity")))
                else:
                    raise InstantiateCSVError("InstantiateCSVError: Файл items.csv поврежден")
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл items.csv")
        except InstantiateCSVError as ice:
            print(ice)

    @classmethod
    def string_to_number(cls, number_sting: str) -> int:
        """
        Преобразование число-строки в число
        :param number_sting: число-строка
        :return: число
        """
        return int(float(number_sting))

    @classmethod
    def normalize_path(cls, file_path: str) -> str:
        temp_path = os.getcwd()
        list_path = temp_path.split("\\")
        i = list_path.index("electronics-shop-project")
        rel_path = "\\".join(list_path[:i+1])+"\\"+file_path
        return os.path.abspath(rel_path)

    def __add__(self, other):
        """
        Сложение кол-ва предметов (quantity)
        экземпляров класса Item и его наследников
        :param other: экземпляр класса Item или его наследника
        :return: число
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("adding variable must be Item or Phone")
