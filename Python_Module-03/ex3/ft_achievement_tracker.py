import random


def gen_player_achievements() -> set[str]:
    achievements: list[str] = give_achievements()
    howm = random.randint(1, len(achievements))
    choice = set(random.sample(achievements, k=howm))
    return choice


def give_achievements() -> list[str]:
    return [
        'Crafting Genius',
        'Strategist',
        'World Savior',
        'Speed Runner',
        'Survivor',
        'Master Explorer',
        'Treasure Hunter',
        'Unstoppable',
        'First Steps',
        'Collector Supreme',
        'Untouchable',
        'Sharp Mind',
        'Boss Slayer',
    ]


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {alice}\n")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}\n")
    print(f"Player Dylan: {dylan}\n")
    print(f"All distinct achievements: {alice.union(bob, charlie, dylan)}")

    common = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {common}\n")

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan: {dylan.difference(alice, bob, charlie)}")

    all_achievements = set(give_achievements())
    print(f"\nAlice is missing: {all_achievements.difference(alice)}\n")
    print(f"Bob is missing: {all_achievements.difference(bob)}\n")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}\n")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}\n")
