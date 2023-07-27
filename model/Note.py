from datetime import date
from enum import Enum


class Note:
    class Priority(Enum):
        lower = 1
        medium = 2
        high = 3

    def __init__(self, id_note: int, title: str, content: str, priority=Priority.lower):
        self.__id = id_note
        self.__title = title
        self.__content = content
        self.__priority = priority
        self.__date_of_create = date.today()
        self.__date_of_update = None

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_content(self):
        return self.__content

    def get_priority(self):
        return self.__priority

    def get_date_of_create(self):
        return self.__date_of_create

    def get_date_of_update(self):
        return self.__date_of_update

    def set_title(self, title: str):
        self.__title = title
        return self

    def set_content(self, content: str):
        self.__content = content
        return self

    def set_priority(self, priority: Priority):
        self.__priority = priority
        return self

    def __str__(self):
        return f'{self.get_title()}\n{self.get_content()}\n{self.get_priority()}\n{self.get_date_of_create()}'
