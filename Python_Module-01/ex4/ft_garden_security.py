#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_height(self, new_height: float) -> None:
        if (new_height < 0):
            print(f"\n{self._name}: Error, height can't"
                  " be negative\nHeight update rejected\n")
        else:
            self._height = new_height
            print(f"Heigh updated: {self._height}cm")

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"{self._name}: Error, age can't"
                  " be negative\nAge update rejected\n")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height)}cm, {self._age} days old")


if __name__ == "__main__":

    rose = Plant("Rose", 25.0, 30)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")

    rose.show()
    rose.set_height(-133.0)
    rose.set_age(-13)

    print("Current state: ", end="")
    rose.show()
