from service.Specification import Specification


class NoteSpecification(Specification):
    def __init__(self, spec: str):
        self.__spec = spec

    def is_satisfied(self, value):
        return self.__spec.lower() in value.lower()