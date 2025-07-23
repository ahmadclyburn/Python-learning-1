
from abc import ABC, abstractmethod
class VehicleInterface(ABC):
    @abstractmethod
    def listAll(self):
        pass
    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def find(self):
        pass