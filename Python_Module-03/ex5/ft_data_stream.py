from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "move", "swim", "climb", "grab"]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list[tuple[str, str]]) -> Generator[tuple[str, str]]:
    while events:
        index = random.randint(0, len(events) - 1)
        event = events[index]
        del events[index]
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    g = gen_event()
    for i in range(0, 1001):
        name, action = next(g)
        print(f"Event {i}: Player {name} did action {action}")

    event_list = [next(g) for _ in range(10)]
    print(f"\nBuilt list of 10 events: {event_list}\n")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}\n")
