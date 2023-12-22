from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Game:
    game_id: int
    subsets: List[Dict[str, int]]

def main():
    with open("input", "r") as f:
        lines = f.read().splitlines()

    games = []
    for l in lines:
        game = parse_game(l)
        games.append(game)

    ret = 0
    checker = GameChecker(12, 14, 13)
    powers = []
    for game in games:
        if checker.is_valid_game(game.subsets):
            ret += game.game_id

        power = checker.get_minimum_cubes_power(game.subsets)
        powers.append(power)

    print(ret)
    print(sum(powers))



def run_tests():
    parsed_game = parse_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert  parsed_game == Game(1, [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}])

    parsed_game = parse_game("Game 100: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert  parsed_game == Game(100, [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}])

    checker = GameChecker(12, 13, 14)

    assert checker.is_valid_game(parsed_game.subsets)

    invalid_game = parse_game("Game 1: 3 blue, 4 red; 1 red, 20 green, 6 blue; 2 green")
    assert not checker.is_valid_game(invalid_game.subsets)

    assert checker.get_minimum_cubes_power(parsed_game.subsets) == 48



def parse_game(line: str):
    parts = line.split(":")
    game_id = int(parts[0].split(" ")[1])

    ret = []
    for r in parts[1].split(";"):
        ret.append({})
        for s in r.split(","):
            num, color = s.strip().split(" ")
            ret[-1][color] = int(num)

    return Game(game_id, ret)



@dataclass
class GameChecker:

    def __init__(self, num_red: int, num_blue: int, num_green: int):
        self._num = {
            "red": num_red,
            "blue": num_blue,
            "green": num_green,
        }

    def is_valid_game(self, subsets: List[Dict[str, int]]):
        for s in subsets:
            for k, v in s.items():
                if v > self._num[k]:
                    return False
        return True

    def get_minimum_cubes_power(self, subsets: List[Dict[str, int]]):
        ret = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for s in subsets:
            for k, v in s.items():
                ret[k] = max(ret[k], v)
        return ret["red"] * ret["green"] * ret["blue"]


if __name__ == "__main__":
    main()
