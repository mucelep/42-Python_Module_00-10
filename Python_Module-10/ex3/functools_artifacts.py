import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]]  = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable[[str], str]]:

    fire = functools.partial(base_enchantment, 50, "Fire")
    ice = functools.partial(base_enchantment, 50, "Ice")
    lightening = functools.partial(base_enchantment, 50, "Lightening")

    return {
        "fire": fire,
        "ice": ice,
        "lightening": lightening
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n negatif olamaz")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) ->str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch

def base_enchantment(power: int, a: str, b: str) -> str:
    return f"{b} received {a} enchantment with {power} power"


def main():
    pass

if __name__ == "__main__":
    main()
