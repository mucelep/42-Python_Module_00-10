#!/usr/bin/env python3

#C'de struct'ın alanları hep public'tir, kim isterse direkt erişip değiştirebilir 
#(rose.height = -999; — hiçbir engel yok). Python'da da varsayılan olarak öyle.
#Ama Python'da alışılagelmiş bir kural (convention) var: bir attribute'un başına tek alt çizgi (_height) koyarsan
#bu diğer programcılara "bu attribute'a dışarıdan doğrudan dokunma, bunun yerine ben (class) sana bunu değiştirmen
#için özel metodlar sunuyorum" mesajı verir.
# Önemli : bu gerçek bir engelleme değil, sadece bir uyarı/anlaşma.

class Plant:
	def __init__(self, name: str, height: float, age: int)-> None:
		self._name = name
		self._height = height
		self._age = age

	def set_height(self, new_height: float)-> None:
		if (new_height < 0):
			print(f"\n{self._name}: Error, height can't be negative\nHeight update rejected\n")##???
		else:
			self._height = new_height
			print(f"Heigh updated: {self._height}cm")

	def set_age(self, new_age: int)-> None:
		if (new_age < 0):
			print(f"{self._name}: Error, age can't be negative\nAge update rejected\n")
		else:
			self._age = new_age
			print(f"Age updated: {self._age} days")

	def get_height(self):
		return self._height

	def get_age(self):
		return self._age

	def show(self):
		print(f"{self._name}: {round(self._height)}cm, {self._age} days old")

if __name__ == "__main__":

	rose = Plant("Rose", 25.0, 30)

	print("=== Garden Security System ===")
	print("Plant created: ", end = "")

	rose.show()
	rose.set_height(-133.0)
	rose.set_age(-13)

	print("Current state: ", end = "")
	rose.show()