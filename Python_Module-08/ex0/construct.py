#!/usr/bin/env python3
import sys
import site
import os

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print(
            "To enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
        )
    else:
        site_packages = site.getsitepackages()[0]
        venv_name = os.path.basename(sys.prefix)

        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}\n")
        print(
            "SUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system.\n"
        )
        print("Package installation path:")
        print(f"{site_packages}")
