import abc
import typing


class DataService(typing.Protocol):
    @abc.abstractmethod
    def create(self, **kwargs):
        pass

    @abc.abstractmethod
    def update(self, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, **kwargs):
        pass
