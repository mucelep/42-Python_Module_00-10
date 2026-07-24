#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 80.0, 20)
    cactus = Plant("Cactus", 45.0, 100)
    sunflower = Plant("Sunflower", 25.0, 50)
    tea = Plant("Tea", 22.0, 10)
    plants = [rose, oak, cactus, sunflower, tea]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
