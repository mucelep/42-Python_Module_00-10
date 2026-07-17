#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant_health() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water_level() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("Testing PlantError...")
    try:
        check_plant_health()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        check_water_level()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    for all_call in (check_plant_health, check_water_level):
        try:
            all_call()
        except GardenError as e:
            print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    test_custom_errors()
    print()
    print("All custom error types work correctly!")
