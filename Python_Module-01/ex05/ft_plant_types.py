#!/usr/bin/env python3

#child class --  class "class_ismi"("parent_class_ismi"):  -- şeklinde yazılır.
class Plant:
	def __init__(self, name: str, height: float, age: int)-> None:
		self.name = name
		self.height = height
		self.age = age
	def show(self)-> None:
		print(f"{self.name}: {self.height}cm , {self.age}days old")

class Flower(Plant):
	def __init__(self, name: str, height: float, age: int, color: str)-> None:
		super().__init__(name, height, age)
		self.color = color
		self.bloomed = False
	def bloom(self)-> None:
		print("[asking the rose to bloom]")
		self.bloomed = True
	def show(self)-> None:
		super().show()
		print(f" Color: {self.color}")
		if not self.bloomed:
			print(" Rose has not bloomed yet")
		else:
			print(" Rose is blooming beautifully!")

class Tree(Plant):
	def __init__(self, name: str, height: float, age: int, trunk_diameter: float)-> None:
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter
	def produce_shade(self)-> None:
		print("[asking the oak to produce shade]")
		print(f"Tree Oak now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide.")
	def show(self)-> None:
		super().show()
		print(f" Trunk diameter: {self.trunk_diameter}cm")

class Vegetable(Plant):
	def __init__(self, name: str, height: float, age: int, harvest_season: str)-> None:
		super().__init__(name, height, age)
		self.harvest_season = harvest_season
		self.nutritional_value = 0
	def show(self)-> None:
		super().show()
		print(f"Harvest season: {self.harvest_season}")
		print(f"Nutritional value: {self.nutritional_value}")
	def grow(self, grow_age: int)-> None:
		print(f"[make tomato grow and age for {grow_age} days]")
		self.age += grow_age
		self.nutritional_value += grow_age

if __name__ == "__main__":
	rose = Flower("Rose", 15.0, 10, "Red")
	oak = Tree("Oak", 200.0, 365, 5.0)
	tomato = Vegetable("Tomato", 5.0, 10, "April")
	print("=== Garden Plant Types ===")
	print("=== Flower")
	rose.show()
	rose.bloom()
	rose.show()
	print("\n=== Tree")
	oak.show()
	oak.produce_shade()
	print("\n=== Vegetable")
	tomato.show()
	tomato.grow(20)
	tomato.show()