#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:# str olarak verilen derece input u int e cevir retrun et
    temp = int(temp_str)
    return temp


def test_temperature(temp: str) -> None:
    print(f"Input data is '{temp}'")
    try:
        value = input_temperature(temp)
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return None


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    print("All tests completed - program didn't crash!")
