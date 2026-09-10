from collections.abc import Callable


def spell_combiner(
        spell1: Callable[[str, int], str],
        spell2: Callable[[str, int], str]
        ) -> Callable[[str, int], tuple[str, str]]:
    def combine(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combine


def power_amplifier(
        base_spell: Callable[[str, int], str],
        multiplier: int
        ) -> Callable[[str, int], str]:
    def amplifie(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifie


def conditional_caster(
        condition: Callable[[str, int], bool],
        spell: Callable[[str, int], str]
        ) -> Callable[[str, int], str]:
    def conditional(target: str, power: int) -> str:
        return (
            spell(target, power)
            if condition(target, power)
            else "Spell fizzled"
            )
    return conditional


def spell_sequence(
        spells: list[Callable[[str, int], str]]
        ) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    def fire(target: str, power: int) -> str:
        return f"Fire attacks hits {target} give {power} demage"

    def water(target: str, power: int) -> str:
        return f"Water attacks hits {target} give {power} demage"

    def heal(target: str, power: int) -> str:
        return f"{target} heals {power} HP"

    def power(target: str, power: int) -> str:
        return str(power)

    print("Testing spell combiner...")
    combine = spell_combiner(fire, heal)
    print(combine("dragon", 10))

    print("\nTesting power amplifier...")
    amp = power_amplifier(power, 3)
    orig = power("dragon", 10)
    amp_val = amp("dragon", 10)
    print(f"Original: {orig}, Amplified: {amp_val}")

    print("\nTesting conditional caster...")
    caster = conditional_caster(lambda t, p: p >= 10, fire)
    print(f'Power 10: {caster("Dragon", 10)}')
    print(f'Power 3: {caster("Dragon", 3)}')

    print("\nTesting spell sequence...")
    seq = spell_sequence([fire, water, heal])
    result_list = seq('Dragon', 15)
    print(f"Sequence: \n{', '.join(result_list)}")


if __name__ == "__main__":
    main()
