def ft_plant_age() -> None:
    try:
        age = int(input("Enter plant age in days: "))
        if age > 60:
            print("Plant is ready to harvest!")
        elif age <= 60:
            print("Plant needs more time to grow.")
    except ValueError:
        print("Please enter a valid days.")
