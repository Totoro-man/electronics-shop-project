class ItemsMixIn:

    def __init__(self, *args):
        super().__init__(*args)
        self.__language = "EN"

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> None:
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
