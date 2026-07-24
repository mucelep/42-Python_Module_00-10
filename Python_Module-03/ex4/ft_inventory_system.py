import sys


def parse_args(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for param in args:
        colon_index = find_colon(param)

        if colon_index == -1 or colon_index == 0:
            print(f"Error - invalid parameter '{param}'")
            continue

        name = param[:colon_index]
        qty_str = param[colon_index + 1:]

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            quantity = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue

        inventory[name] = quantity
    return inventory


def find_colon(param: str) -> int:
    i = 0
    while i < len(param):
        if param[i] == ':':
            return i
        i += 1
    return -1


def find_most(inventory: dict[str, int]) -> None:
    most_name = ""
    most_value = -1
    for name in inventory.keys():
        quant = inventory[name]
        if quant > most_value:
            most_value = quant
            most_name = name
    print(f"Item most abundant: {most_name} with quantity {most_value}")


def find_least(inventory: dict[str, int]) -> None:
    least_name = ""
    least_value = -1
    for name in inventory.keys():
        quant = inventory[name]
        if least_value == -1 or quant < least_value:
            least_value = quant
            least_name = name
    print(f"Item most abundant: {least_name} with quantity {least_value}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")

    inventory = parse_args(sys.argv[1:])
    print(f"Got inventory: {inventory}")
    print(f"Item List: {inventory.keys()}")
    totalq = sum(inventory.values())
    print(f"Total quantity of the {len(inventory.keys())}"
          f" items: {totalq}")

    for item in inventory.keys():
        quant = inventory[item]
        percentage: float = round((quant / totalq) * 100, 1)
        print(f"Item {item} represents {percentage}%")

    find_most(inventory)
    find_least(inventory)

    inventory.update({'megic_item': 1})
    print(f"Updated inventory: {inventory}")
