from Notes_app.service.Specification import Specification


class TitleSpecification(Specification):
    def __init__(self, title: str):
        self.__title = title

    def is_satisfied(self, value):
        return self.__title.lower() in value.lower()
