from abc import ABC, abstractmethod


class Creatures(ABC):
    def __init__(self, name: str, c_type: str) -> None:
        self.name = name
        self.type = c_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self, ) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creatures):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creatures):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creatures):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creatures):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
