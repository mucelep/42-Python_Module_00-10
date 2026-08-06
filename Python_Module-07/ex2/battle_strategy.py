from abc import ABC, abstractmethod
from ex0.creatures import Creatures
from ex1.capabilities import TransformCapability, HealCapability
from .exception import InvalidTypeError


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creatures) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creatures) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creatures) -> bool:
        return isinstance(creature, Creatures)

    def act(self, creature: Creatures) -> str:
        if not self.is_valid(creature):
            raise InvalidTypeError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )

        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creatures) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creatures) -> str:
        if not self.is_valid(creature):
            raise InvalidTypeError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )

        assert isinstance(creature, TransformCapability)

        result = ""
        result += creature.transform() + "\n"
        result += creature.attack() + "\n"
        result += creature.revert()
        return result


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creatures) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creatures) -> str:
        if not self.is_valid(creature):
            raise InvalidTypeError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )

        assert isinstance(creature, HealCapability)

        result = ""
        result += creature.attack() + "\n"
        result += creature.heal()
        return result
