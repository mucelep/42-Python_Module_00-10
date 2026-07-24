#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, agee: int) -> None:
        self.name = name
        self.height = height
        self._age = agee
        self.stats = Plant.Stats(self.name)

    class Stats:
        def __init__(self, name: str) -> None:
            self.name = name
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self) -> None:
            print(f"statistics for {self.name}")
            print(f"stats: {self.grow_count} grow,"
                  f" {self.age_count} age,  {self.show_count} show")

    @staticmethod
    def older_year(age: int) -> bool:
        result: bool = age > 365
        print(f"Is {age} days more than a year? -> {result}")
        return result

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self._age} days old")
        self.stats.show_count += 1

    def grow(self, gr: float) -> None:
        print(f"[asking the {self.name} to grow and bloom]")
        self.height += gr
        self.stats.grow_count += 1

    def age(self, n_age: int) -> None:
        self._age += n_age
        self.stats.age_count += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed: bool = False

    def bloom(self) -> None:
        print("[asking the rose to grow and bloom]")
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color {self.color}")
        if not self.bloomed:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beatuifully!")


class Tree(Plant):

    class Tree_Stats(Plant.Stats):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            self.shade_count = 0
            
        def display(self) -> None:
            super().display()
            print(f"{self.shade_count} shade")

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.t_stats = Tree.Tree_Stats(name)

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height}cm long and {self.trunk_diameter}cm wide.")
        self.t_stats.shade_count += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str, num_seeds: int) -> None:
        super().__init__(name, height, age, color)
        self.num_seeds = 0

    def bloom(self) -> None:
        print(f"[make {self.name} grow, age and bloom]")
        super().bloom()
        self.num_seeds = 42

    def show(self) -> None:
        super().show()
        print(f"seeds: {self.num_seeds}")


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, "Red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    unknown = Plant.create_anonymous()
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.older_year(30)
    Plant.older_year(400)

    print("\n=== Flower")
    rose.show()
    rose.stats.display()
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    rose.stats.display()

    print("\n=== Tree")
    oak.show()
    oak.t_stats.display()
    oak.produce_shade()
    oak.t_stats.display()

    print("\n=== Seed")
    sunflower.show()
    sunflower.bloom()
    sunflower.age(20)
    sunflower.grow(30)
    sunflower.show()
    sunflower.stats.display()

    print("\n=== Anonymous")
    unknown.show()
    unknown.stats.display()
