#!/usr/bin/env python3
import sys
import importlib
import importlib.metadata


DEPENDENCIES: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }


def check_dependencies(dep: dict[str, str]) -> bool:
    """Verifies each required package is importable and prints its version."""
    missing: bool = False

    for package, message in dep.items():
        try:
            importlib.import_module(package)
            version = importlib.metadata.version(package)
            print(f"[OK] {package} ({version}) - {message}")
        except ModuleNotFoundError:
            print(f"[NO] {package} is missing!")
            missing = True

    return missing


def visualization() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    data = np.random.randint(0, 100, 1000)
    df = pd.DataFrame({"signal": data})
    print(f"Processing {len(df)} data points...")

    plt.figure(figsize=(9, 5))
    plt.plot(df["signal"])
    plt.title("Matrix Signal")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")

def main():
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    is_missing = check_dependencies(DEPENDENCIES)
    if is_missing:
        print("\nMissing dependencies detected!")
        print("Install via pip: pip install -r requirements.txt")
        print("Install via poetry: poetry install")
        sys.exit()
    else:
        print("\nAnalyzing Matrix data...")
        visualization()
        print("Generating visualization...")
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
