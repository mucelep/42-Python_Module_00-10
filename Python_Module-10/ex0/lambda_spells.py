from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = sorted(
        artifacts,
        key=lambda x: x["power"], reverse=True)
    return result


def power_filter(mages: list[dict[str, Any]], min_power: int
                 ) -> list[dict[str, Any]]:
    result = filter(lambda mage: mage["power"] > min_power, mages)
    return list(result)


def spell_transformer(spells: list[str]) -> list[str]:
    result = map(lambda spell: "* "+spell+" *", spells)
    return list(result)


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    hpower = max(mages, key=lambda m: m["power"])
    lpower = min(m["power"] for m in mages)
    average = round(sum(m["power"] for m in mages) / len(mages), 2)
    return {
        "max_power": int(hpower["power"]),
        "min_power": int(lpower["power"]),
        "avg_power": float(average)
    }


def main() -> None:
    print("Testing artifact sorter...")
    fire = {
        "name": "Fire Staff",
        "power": 92,
        "tpye": "fire"
    }

    orb = {
        "name": "Crystal Orb",
        "power": 85,
        "tpye": "Crystal"
    }

    x = artifact_sorter([fire, orb])
    print(f'{x[0]["name"]}({x[0]["power"]} power) comes'
          f'before {x[1]["name"]} ({x[1]["power"]} power)\n')

    print("Testing spell transformer...")
    trans = spell_transformer(["fireball", "heal", "shield"])
    print(" ".join(trans))


if __name__ == "__main__":
    main()
