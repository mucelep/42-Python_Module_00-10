#!/usr/bin/env python3

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
	def show(self):
		print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
	print("=== Garden Plant Registry ===")

	rose = Plant("Rose", 25, 30)
	sunflower = Plant("Sunflower", 150, 60)
	cactus = Plant("Cactus", 10, 365)

	rose.show()
	sunflower.show()
	cactus.show())