from abc import abstractmethod, ABCMeta
import json
import pickle


class SerializationInterface(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, file):
        pass
    
    @abstractmethod
    def serialize(self, container):
        pass


class JsonSerialization(SerializationInterface):

    def __init__(self, file):
        self.file = file
    
    def serialize(self, container):
        with open(self.file, "w") as fh:
            json.dump(container, fh)


class BinSerialization(SerializationInterface):

    def __init__(self, file):
        self.file = file
    
    def serialize(self, container):
        with open(self.file, "wb") as fh:
            pickle.dump(container, fh)