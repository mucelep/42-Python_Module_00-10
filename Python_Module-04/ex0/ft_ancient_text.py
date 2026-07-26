import typing
import sys


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file: typing.IO = open(sys.argv[1])
            print("---")
            print(file.read())
            print("---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
        except FileNotFoundError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
