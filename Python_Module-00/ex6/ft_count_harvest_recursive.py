def ft_count_harvest_recursive() -> None:
    try:
        day = int(input("Days until harvest: "))
        recursive(1, day)
        print("Harvest time!")
    except ValueError:
        print("Please enter a valid days.")


def recursive(i: int, day: int) -> None:
    if i > day:
        return
    print("Day:", i)
    recursive(i + 1, day)
