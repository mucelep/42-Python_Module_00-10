#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, height: float, age: int, grow_rate: float) -> None:
		self.name = name
		self.height = height
		self.agee = age
		self.grow_rate = grow_rate
	def show(self)-> None:
		print(f"{self.name}: {round(self.height,2)}cm, {self.agee} days old")
	def grow(self)-> None:
		self.height += self.grow_rate
	def age(self)-> None:
		self.agee += 1

if __name__ == "__main__":
	print("=== Garden Plant Growth ===")
	rose = Plant("Rose", 25.0, 30, 0.8)
	rose.show()
	start = rose.height
	for i in range(1,8):
		print(f"=== Day {i} ===")
		rose.grow()
		rose.age()
		rose.show()
	print(f"\nGrowth this week: {round(rose.height - start, 2)}cm")