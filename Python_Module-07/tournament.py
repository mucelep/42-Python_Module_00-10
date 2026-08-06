from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2 import InvalidTypeError, BattleStrategy


def battle(opponent: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponent)}opponents involved")

    fighters = [(factory.create_base(), strategy)
                for factory, strategy in opponent]

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            creature_a, strategy_a = fighters[i]
            creature_b, strategy_b = fighters[j]

            print("\n* Battle *")
            print(creature_a.describe())
            print("vs.")
            print(creature_b.describe())
            print("now fight!")
            try:
                print(strategy_a.act(creature_a))
                print(strategy_b.act(creature_b))
            except InvalidTypeError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    cf_flame = FlameFactory()
    cf_aqua = AquaFactory()
    cf_heal = HealingCreatureFactory()
    cf_trans = TransformCreatureFactory()

    s_normal = NormalStrategy()
    s_aggr = AggressiveStrategy()
    s_def = DefensiveStrategy()

    print("Tournament 0 (basic)")
    battle([
        (cf_flame, s_normal),
        (cf_heal, s_def),
    ])

    print("\nTournament 1 (error)")
    battle([
        (cf_flame, s_aggr),
        (cf_heal, s_def),
    ])

    print("\nTournament 2 (multiple)")
    battle([
        (cf_aqua, s_normal),
        (cf_heal, s_def),
        (cf_trans, s_aggr),
    ])


if __name__ == "__main__":
    main()
