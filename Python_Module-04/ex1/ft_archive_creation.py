#!/usr/bin/env python3
import sys
import typing


def save_file() -> str:
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file: typing.IO = open(sys.argv[1])
        print("---")
        text = file.read()
        print(text)
        print("---")
        file.close()
        print(f"File '{sys.argv[1]} closed.'")
        return text
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return ""
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return ""


def copy_file(text: str) -> None:
    print("Transform data:")
    new_text = ""
    for char in text:
        if char == "\n":
            new_text += "#\n"
        else:
            new_text += char
    if len(text) > 0 and text[-1] != "\n":
        new_text += "#"
    print("---")
    print(f"{new_text}")
    print("---")
    file_name = input("Enter new file name (or empty): ")
    if file_name == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{file_name}'")
        new_file = open(file_name, "w")
        new_file.write(new_text)
        new_file.close()
        print(f"Data saved in file '{file_name}'.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        text = save_file()
        print()
        copy_file(text)