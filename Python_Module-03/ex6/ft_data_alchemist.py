import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")

    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
               'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}\n")

    captilaze_list: list[str] = [x.capitalize() for x in players]
    print(f"New list with all names capitalized: {captilaze_list}\n")

    captilaze_only: list[str] = [x for x in players if x[0].isupper()]
    print(f"New list of capitalized names only: {captilaze_only}\n")

    score_dict = {name: random.randint(0, 1000) for name in captilaze_list}
    print(f"Score dict: {score_dict}\n")

    score_average = round(sum(score_dict[name] for name in score_dict)
                          / len(score_dict), 2)
    print(f"Score average is {score_average}\n")

    score_overavarage = {name: score_dict[name] for name in score_dict
                         if score_dict[name] > score_average}
    print(f"High scores: {score_overavarage}")
