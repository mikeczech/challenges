from typing import List
import re
from collections import deque

def main():
    with open("input", "r") as f:
        cards = f.read().splitlines()
    print(determine_points(cards))
    print(determine_cards(cards))

def run_tests():
    cards = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]

    result = determine_points(cards)
    assert result == 13

    result = determine_cards(cards)
    assert result == 30

def parse_card(card: str):
    card = re.sub(' +', ' ', card)
    game, numbers = card.split(":")
    game_id = int(game.split(" ")[1].strip())
    winning_numbers, your_numbers = numbers.split("|")

    winning_numbers = [int(x) for x in winning_numbers.strip().split(" ") if len(x) > 0]
    your_numbers = [int(x) for x in your_numbers.strip().split(" ") if len(x) > 0]

    return game_id, winning_numbers, your_numbers


def determine_points(cards: List[str]):
    ret = 0

    for c in cards:
        _, winning_numbers, your_numbers = parse_card(c)
        num_matches = len(set(winning_numbers) & set(your_numbers))
        if num_matches > 0:
            ret += 2**(num_matches - 1)

    return ret


def determine_cards(initial_cards: List[str]):
    cards = {}
    max_game_id = 0
    for c in initial_cards:
        game_id, winning_numbers, your_numbers = parse_card(c)
        cards[game_id] = (winning_numbers, your_numbers)
        max_game_id = max(game_id, max_game_id)

    ret = 0
    queue = deque(list(cards.keys()))
    while len(queue) > 0:
        game_id = queue.popleft()
        ret += 1
        winning_numbers, your_numbers = cards[game_id]
        num_matches = len(set(winning_numbers) & set(your_numbers))
        for i in range(1, num_matches + 1):
            if i <= max_game_id:
                queue.append(i + game_id)

    return ret


if __name__ == "__main__":
    main()
