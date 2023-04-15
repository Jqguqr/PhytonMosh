# Import abstract module abc
from abc import ABC, abstractmethod


# Create aour self Exception
class InvalidOperationError(Exception):
    pass


# Making Stream Abstract class
class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already close.")
        self.opened = False

    # Interface
    @abstractmethod
    def read(self):
        pass
    # Una vez declarada la clase Stream y su metodo read como abstract,
    # para poder heredar a otra clase tenemos que implementar
    # (override o sobrescribir el metodo read) el metodo read en la clase hija
    # de lo contrario la clase hija sera abstracta y no podremos nstanciar


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Conecting to a network")


class MemoryStream
