#!/usr/bin/env python3
import sys
import importlib, importlib.metadata


DEPENDENCIES: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }

def check_dependencies(dep: dict[str, str]) -> bool:
    missing: bool = False

    for package, message in dep.items():
        try:
            module = importlib.import_module(package)
            version = importlib.metadata.version(package)
            print(f"[OK] {package} ({version}) - {message}")
        except ModuleNotFoundError:
            print(f"[NO] {package} is missing!")
            missing = True

    return missing


def main():
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    is_missing = check_dependencies(DEPENDENCIES)
    if is_missing:
        print(f"\nMissing dependencies detected!")
        print("Install via pip: pip install -r requirements.txt")
        print("Install via poetry: poetry install")
        sys.exit()
    else:
        pass

if __name__ == "__main__":
    main()