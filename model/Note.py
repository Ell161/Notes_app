from datetime import date


class Note:
    def __init__(self, id_note: int, title: str, content: str, date_create: str, date_update: str = None):
        self.__id = id_note
        self.__title = title
        self.__content = content
        self.__date_of_create = date_create
        self.__date_of_update = date_update

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_content(self):
        return self.__content

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

    def set_date_of_update(self):
        self.__date_of_update = str(date.today())
        return self

    def get_data(self):
        return {'id': self.__id,
                'title': self.__title,
                'content': self.__content,
                'date_of_create': self.__date_of_create,
                'date_of_update': self.__date_of_update
                }
