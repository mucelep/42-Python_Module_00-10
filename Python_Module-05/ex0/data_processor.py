#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) ->None:
        self._storage: list[str] = []
        self._total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No Data to output")
        value = self._storage.pop(0)
        total = (self._total - len(self._storage)) - 1
        return (total, value)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            print(f"Processing data: {data}")
            for item in data:
                self._storage.append(str(item))
                self._total += 1
        else:
            print(f"Processing data: {data}")
            self._storage.append(str(data))
            self._total += 1


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric text")
        if isinstance(data, list):
            print(f"Processing data: {data}")
            for item in data:
                self._storage.append(item)
                self._total += 1
        else:
            print(f"Processing data: {data}")
            self._storage.append(data)
            self._total += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str):
                    return False
                if not isinstance(value, str):
                    return False
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                if isinstance(item, dict):
                    for key, value in item.items():
                        if not isinstance(key, str):
                            return False
                        if not isinstance(value, str):
                            return False
            return True
        else:
            return False


    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            print(f"Processing data: {data}")
            for item in data:
                formatted = f"{item['log_level']}: {item['log_message']}"
                self._storage.append(formatted)
                self._total += 1
        else:
            print(f"Processing data: {data}")
            formatted = f"{data['log_level']}: {data['log_message']}"
            self._storage.append(formatted)
            self._total += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Testing Numeric Processor...\n")
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'hello': {numeric.validate("hello")}")

    print(f"\nTest invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        total, value = numeric.output()
        print(f"Numeric value {total}: {value}")


    print("\nTesting Text Processor...\n")
    print(f"Trying to validate input '42': {text.validate(42)}")
    try:
        text.ingest(['Hello', 'Nexus', 'World'])
    except ValueError as e:
        print(f"Got exception: {e}")
    print("Extracting 1 values...")
    total, value = text.output()
    print(f"text value {total}: {value}")


    print("\nTesting Text Processor...\n")
    print(f"Trying to validate input 'Hello': {log.validate("hello")}")
    try:
        log.ingest([{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, 
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}])
    except ValueError as e:
        print(f"Got exception: {e}")

    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {total}: {value}")