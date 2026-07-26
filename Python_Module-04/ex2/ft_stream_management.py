#!/usr/bin/env python3
import sys
import typing


def save_file() -> str:
    sys.stdout.write(f"Accessing file '{sys.argv[1]}'\n")
    try:
        file: typing.IO = open(sys.argv[1])
        sys.stdout.write("---\n")
        text = file.read()
        sys.stdout.write(f"{text}\n")
        sys.stdout.write("---\n")
        file.close()
        sys.stdout.write(f"File '{sys.argv[1]} closed.'\n")
        return text
    except FileNotFoundError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
        return ""
    except PermissionError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
        return ""


def copy_file(text: str) -> None:
    sys.stdout.write("Transform data:\n")
    new_text = ""
    for char in text:
        if char == "\n":
            new_text += "#\n"
        else:
            new_text += char
    if len(text) > 0 and text[-1] != "\n":
        new_text += "#"
    sys.stdout.write("---\n")
    sys.stdout.write(f"{new_text}\n")
    sys.stdout.write("---\n")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    file_name = sys.stdin.readline()
    file_name = file_name[:-1]
    if file_name == "":
        sys.stdout.write("Not saving data.\n")
    else:
        try:
            sys.stdout.write(f"Saving data to '{file_name}'\n")
            new_file = open(file_name, "w")
            new_file.write(f"{new_text}\n")
            new_file.close()
            sys.stdout.write(f"Data saved in file '{file_name}'.\n")
        except PermissionError as e:
            sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {e}\nData not saved.")


if __name__ == "__main__":
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    if len(sys.argv) == 1:
        sys.stdout.write("Usage: ft_ancient_text.py <file>\n")
    else:
        text = save_file()
        sys.stdout.write("\n")
        copy_file(text)