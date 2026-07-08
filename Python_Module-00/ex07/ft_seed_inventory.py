def	ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit == "packets":
		print("%s seeds: %d packets available" % (seed_type.capitalize() ,quantity))
	elif unit == "grams":
		print("%s seeds: %d grams total" % (seed_type.capitalize() ,quantity))
	elif unit == "area":
		print("%s seeds: covers %d square meters" % (seed_type.capitalize() ,quantity))
	else:
		print("Unknown unit type")
