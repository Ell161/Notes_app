from service.Specification import Specification


class ContentSpecification(Specification):
    def __init__(self, content: str):
        self.__content = content

    def is_satisfied(self, value):
        return self.__content.lower() in value.lower()
