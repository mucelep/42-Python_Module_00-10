#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream():

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            hendled = False
            for processor in self._processors:
                if processor.validate(data):
                    processor.ingest(data)
                    hendled = True
                    break
            if not hendled:
                 print(f"DataStream error - Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
        for processor in self._processors:
            name = type(processor).__name__.replace("Processor", " Processor")
            total = processor._total
            remaining = len(processor._storage)
            print(f"{name}: total {total} items processed, remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            collected: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    collected.append(processor.output())
                except IndexError:
                    break
            if collected:
                plugin.process_output(collected)
                

class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        cvs = ",".join(values)
        print(f"CSV Output:\n  {cvs}")


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [f'"item_{rank}": "{item}"' for rank, item in data]   
        json = "{" + ", ".join(values) + "}" 
        print(f"JSON Output:\n  {json}")



if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    stream = DataStream()

    print("Initialize Data Stream...")
    stream.print_processors_stats()
    
    data1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]
  
    print("\nRegistering data processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    print(
        "\nSend first batch of data on stream: "
        "['Hello world', [3.14, -1, 2.71], "
        "[{'log_level': 'WARNING', "
        "'log_message': 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', 'log_message': 'User wil is connected'}], "
        "42, ['Hi', 'five']]\n"
    )
    stream.process_stream(data1)
    stream.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()

    print(
        "\nSend another batch of data: [21, ['I love AI', "
        "'LLMs are wonderful', 'Stay healthy'],"
        " [{'log_level': 'ERROR', 'log_message': '500 server crash'}, "
        "{'log_level': 'NOTICE',"
        " 'log_message': 'Certificate expires in 10 days'}], "
        "[32, 42, 64, 84, 128, 168], 'World hello']\n"
    )
    data_2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    stream.process_stream(data_2)
    stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:\n")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()
