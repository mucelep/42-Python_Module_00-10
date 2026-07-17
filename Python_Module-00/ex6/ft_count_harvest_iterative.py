def ft_count_harvest_iterative() -> None:
    try:
        day = int(input("Days until harvest: "))
        for i in range(1, day + 1):
            print("Day", i)
        print("Harvest time!")
    except ValueError:
        print("Please enter a valid days.")
