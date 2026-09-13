import functools
import time
from collections.abc import Callable
from typing import Any

def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def time_wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        func_result = func(*args, **kwargs)
        execution_duration = time.time() - start_time
        print(f"Spell completed in {execution_duration:.3f} seconds")
        return func_result
    return time_wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    """It finds the power value of the
       argument and compares it with min_power."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")
            if power is None:
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break
            if power is not None and power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    """ fonksiyon bir hata verirse belli bir deneme sayısında tekrar dener"""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                            )
                attempt += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        valid_length = len(name.strip()) >= 3
        valid_char = all(c.isalpha() or c.isspace() for c in name)
        return valid_length and valid_char

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"




def main() -> None:
    print("Testing spell timer..")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(result)

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def crash_spell() -> None:
        raise RuntimeError("Spell failed")
    print(crash_spell())
    print("Waaaaaaagh spelled !\n")

    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(mage.validate_mage_name("bacomaco de"))
    print(mage.validate_mage_name("bacomaco d3"))
    print(mage.cast_spell("fireman",15))
    print(mage.cast_spell("owyesman",5))


if __name__ == "__main__":
    main()