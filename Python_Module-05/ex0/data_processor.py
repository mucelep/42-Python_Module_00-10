#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):

    def __init__(self) ->None:
        self._storage: list[str] = []
        self._rank: int = 0

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
        rank = (self._rank - len(self._storage)) - 1
        return (rank, value)

class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            print(f"Processing data: {data}")
            for item in data:
                self._storage.append(str(item))
                self._rank += 1
        else:
            print(f"Processing data: {data}")
            self._storage.append(str(data))
            self._rank += 1

class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric text")
        if isinstance(data, list):
            print(f"Processing data: {data}")
            for item in data:
                self._storage.append(item)
                self._rank += 1
        else:
            print(f"Processing data: {data}")
            self._storage.append(data)
            self._rank += 1

class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        pass

if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    numeric = NumericProcessor()
    text = TextProcessor()

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
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")


    print("\nTesting Text Processor...\n")
    print(f"Trying to validate input '42': {text.validate(42)}")
    text.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 values...")
    rank, value = text.output()
    print(f"text value {rank}: {value}")

    print("\nTesting Text Processor...\n")