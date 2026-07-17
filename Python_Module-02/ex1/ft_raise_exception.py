#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:# str olarak verilen derece input u int e cevir retrun et
    temp = int(temp_str)#abc girilirse burda patlıyor alta inmiyor
    if temp >= 0 and temp <= 40:
        return temp
    elif temp > 40:
        raise ValueError(f" {temp}°C is too hot for plants (max 40°C)")#raise, "burada bir hata oluştu, bu hatayı fırlat" demektir.
    else:
        raise ValueError(f" {temp}°C is too cold for plants (min 0°C)")


def test_temperature(temp: str) -> None:
    print(f"Input data is '{temp}'")
    try:
        value = input_temperature(temp)
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return None


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    test_temperature("100")
    print()
    test_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")
