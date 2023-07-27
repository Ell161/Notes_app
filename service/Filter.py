import abc
import typing


class Filter(typing.Protocol):
    @abc.abstractmethod
    def filter(self, items, specification):
        pass
