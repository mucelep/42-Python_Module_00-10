from abc import ABC, abstractmethod
from .creatures import Flameling, Pyrodon, Aquabub, Torragon, Creatures


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creatures:
        pass

    @abstractmethod
    def create_evolved(self) -> Creatures:
        pass


class FlameFactory(CreatureFactory):

    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
