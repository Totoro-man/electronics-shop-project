class ItemsMixIn:
    """
    Класс для добавления функциональности потомкам класса Item.
    """
    def __init__(self, *args):
        """
        Создание экземпляра класса ItemsMixIn.
        Добавление свойства language
        """
        super().__init__(*args)
        self.__language = "EN"

    """
    Getter для Item.__language
    """
    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> None:
        """
        Переключает язык с EN на RU и обратно
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
