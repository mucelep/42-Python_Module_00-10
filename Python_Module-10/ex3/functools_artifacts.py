import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
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
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def base_enchantment(a: int, b: str, c: str) -> str:
    return f"{c} is enchanted with {b} at {a} power"


def main() -> None:
    print("Testing spell reducer...")
    print(f'sum: {spell_reducer([10,20,30,40], "add")}')
    print(f'Product: {spell_reducer([10,20,30,40], "multiply")}')
    print(f'max: {spell_reducer([10,20,30,40], "max")}')

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"]("sword"))
    print(enchanters["ice"]("sword"))
    print(enchanters["lightening"]("sword"))

    print("\nTesting memoized fibonacci...")
    print(f"fib(0): {memoized_fibonacci(0)}")
    print(f"fib(1): {memoized_fibonacci(1)}")
    print(f"fib(10): {memoized_fibonacci(10)}")
    print(f"fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "iceball", "waterball"]))
    print(dispatcher({"1": 2}))


if __name__ == "__main__":
    main()
