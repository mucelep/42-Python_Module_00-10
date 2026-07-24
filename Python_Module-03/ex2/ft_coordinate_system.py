import math


def calculate_distance(pos1: tuple[float, float, float],
                       pos2: tuple[float, float, float]) -> float:
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    dz = pos1[2] - pos2[2]
    return math.sqrt(dx**2 + dy**2 + dz**2)


def get_player_pos() -> tuple[float, float, float]:
    while True:
        cordinat: str = input("Enter new coordinates as floats"
                              " in format 'x,y,z': ")
        parts = cordinat.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0])
        except ValueError as e:
            print(f"Error on parameter '{parts[0]}': {e}")
            continue

        try:
            y = float(parts[1])
        except ValueError as e:
            print(f"Error on parameter '{parts[1]}': {e}")
            continue

        try:
            z = float(parts[2])
        except ValueError as e:
            print(f"Error on parameter '{parts[2]}': {e}")
            continue

        return (x, y, z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos}")
    print(f"It includes: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")
    center: tuple[float, float, float] = (0.0, 0.0, 0.0)
    dist_center: float = calculate_distance(center, pos)
    print(f"Distance to center: {round(dist_center, 4)}")

    print("\nGet a second set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    dist_between = calculate_distance(pos, pos1)
    print("Distance between the 2 sets of coordinates:"
          f" {round(dist_between, 4)}")
