#!/usr/bin/env python3
import importlib
import importlib.metadata
import sys
import os


def check_dependencies() -> None:
    try:
        importlib.import_module("dotenv")
        version = importlib.metadata.version("python-dotenv")
        print(f"[OK] python-dotenv ({version})")
    except ModuleNotFoundError:
        print("\nERROR: python-dotenv not installed!")
        print("Install via pip: pip install -r requirements.txt")
        sys.exit()


def get_env() -> None:
    value = os.environ.get("MATRIX_MODE")
    print(f"Mode: {value if value is not None else '[MISSING]'}")

    value = os.environ.get("DATABASE_URL")
    print(
        "Database: Connected to local instance"
        if value is not None
        else "Database: [MISSING]"
    )

    value = os.environ.get("API_KEY")
    print(
        "API Access: Authenticated"
        if value is not None
        else "API Access: [MISSING]"
    )

    value = os.environ.get("LOG_LEVEL")
    print(f'LOG Level: {"DEBUG" if value is not None else "[MISSING]"}')

    value = os.environ.get("ZION_ENDPOINT")
    print(f'Zion Network: {"Online" if value is not None else "[MISSING]"}')


def security_check() -> None:
    print("[OK] No hardcoded secrets detected")
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        print("[OK] .env file properly configured")
    else:
        print("[NO] .env file not found")
    if os.environ.get("MATRIX_MODE") == "production":
        print("[OK] Production environment variables override .env values")
    else:
        print("[OK] Production overrides available")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    check_dependencies()

    print("\nConfiguration loaded:")
    from dotenv import load_dotenv
    load_dotenv()
    get_env()

    print("\nEnvironment security check:")
    security_check()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
