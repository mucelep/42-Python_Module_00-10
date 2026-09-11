from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    def accumulator(power_amount: int) -> int:
        nonlocal initial_power
        initial_power += power_amount
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable[..., Any]]:
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("store 'secret' = 42")
    print(f"recall 'secret': {vault["recall"]("secret")}")
    print(f"recall 'unknown': {vault["recall"]("unknown")}")

    print("\nTesting enchantment factory...")
    flame = enchantment_factory("Flameing")
    print(flame("sword"))
    print(flame("armor"))


if __name__ == "__main__":
    main()
