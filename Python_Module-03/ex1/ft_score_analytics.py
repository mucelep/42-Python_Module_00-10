import sys


def to_int(args: list[str]) -> list[int]:
    valid_scores: list[int] = []
    for i in args:
        try:
            valid_scores.append(int(i))
        except ValueError:
            print(f"Invalid parameter: '{i}'")
    return valid_scores


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print(f"No scores provided. Usage: python3 {sys.argv[0]}"
              " <score1> <score2> ...")
    else:
        scores: list[int] = to_int(sys.argv[1:])
        if len(scores) == 0:
            print(f"No scores provided. Usage: python3 {sys.argv[0]}"
                  " <score1> <score2> ...")
        else:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(sys.argv) - 1}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {float(sum(scores) / len(scores)):.2f}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
