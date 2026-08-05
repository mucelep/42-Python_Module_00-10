from ex0 import FlameFactory, AquaFactory, CreatureFactory


def factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing factory")
    for creature in [base, evolved]:
        print(creature.describe())
        print(creature.attack())
    print()


def battle(factory1: CreatureFactory,
           factory2: CreatureFactory) -> None:
    creature_a = factory1.create_base()
    creature_b = factory2.create_base()

    print("Testing battle")
    print(creature_a.describe())
    print("vs.")
    print(creature_b.describe())
    print("Fight!")
    print(creature_a.attack())
    print(creature_b.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    factory(flame_factory)
    factory(aqua_factory)
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
