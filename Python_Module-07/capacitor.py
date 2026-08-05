from ex1 import HealingCreatureFactory, TransformCreatureFactory


def healcreaturesfac(factory: HealingCreatureFactory) -> None:
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print("Testing Creature with healing capability")
    print("Base:")

    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.heal())

    print("Evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.heal())
    print()


def transcreaturesfac(factory: TransformCreatureFactory) -> None:
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print("Testing Creature with transform capability")
    print("Base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())

    print("Evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.attack())
    print(evolved_creature.revert())


def main() -> None:
    healfac = HealingCreatureFactory()
    transfac = TransformCreatureFactory()
    healcreaturesfac(healfac)
    transcreaturesfac(transfac)


if __name__ == "__main__":
    main()
