from typing import List
from collections import defaultdict

def main_part_one():
    with open("input", "r") as f:
        schematic = f.read().splitlines()
    sum_ = part_number_sum_part_one(schematic)
    print(sum_)

def main_part_two():
    with open("input", "r") as f:
        schematic = f.read().splitlines()
    sum_ = part_number_sum_part_two(schematic)
    print(sum_)


def run_tests_part_one():
    schematic = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]

    sum_ = part_number_sum_part_one(schematic)

    assert sum_ == 4361


def run_tests_part_two():
    schematic = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]

    sum_ = part_number_sum_part_two(schematic)

    assert sum_ == 467835


def is_number(c: str):
    return ord(c) >= 48 and ord(c) <= 57

def is_symbol(c: str):
    if ord(c) >= 48 and ord(c) <= 57:
        return False
    if c == ".":
        return False
    return True

def is_gear(c: str):
    return c == "*"

def part_number_sum_part_one(schematic: List[str]):
    ret = 0
    for i in range(len(schematic)):
        digits = []
        is_adj_to_symbol = False
        for j in range(len(schematic[i])):
            if is_number(schematic[i][j]):
                digits.append(schematic[i][j])
                is_adj_to_symbol = (
                    ((i-1 >= 0) and is_symbol(schematic[i-1][j])) or
                    ((i+1 < len(schematic)) and is_symbol(schematic[i+1][j])) or
                    ((j-1 >= 0) and is_symbol(schematic[i][j-1])) or
                    ((j+1 < len(schematic[i])) and is_symbol(schematic[i][j+1])) or
                    ((i-1 >= 0) and (j-1 >= 0) and is_symbol(schematic[i-1][j-1])) or
                    ((i+1 < len(schematic)) and (j+1 < len(schematic[i])) and is_symbol(schematic[i+1][j+1])) or
                    ((j-1 >= 0) and (i+1 < len(schematic)) and is_symbol(schematic[i+1][j-1])) or
                    ((i-1 >= 0) and (j+1 < len(schematic[i])) and is_symbol(schematic[i-1][j+1])) or
                    is_adj_to_symbol
                )
            else:
                if len(digits) > 0 and is_adj_to_symbol:
                    ret += int("".join(digits))
                digits = []
                is_adj_to_symbol = False

        if len(digits) > 0 and is_adj_to_symbol:
            ret += int("".join(digits))

    return ret


def part_number_sum_part_two(schematic: List[str]):
    gears = defaultdict(list)
    for i in range(len(schematic)):
        digits = []
        is_adj_to_gears = set()
        for j in range(len(schematic[i])):
            if is_number(schematic[i][j]):
                digits.append(schematic[i][j])

                if ((i-1 >= 0) and is_gear(schematic[i-1][j])):
                    is_adj_to_gears.add((i-1,j))

                if ((i+1 < len(schematic)) and is_gear(schematic[i+1][j])):
                    is_adj_to_gears.add((i+1,j))

                if ((j-1 >= 0) and is_gear(schematic[i][j-1])):
                    is_adj_to_gears.add((i,j-1))

                if ((j+1 < len(schematic[i])) and is_gear(schematic[i][j+1])):
                    is_adj_to_gears.add((i,j+1))

                if ((i-1 >= 0) and (j-1 >= 0) and is_gear(schematic[i-1][j-1])):
                    is_adj_to_gears.add((i-1,j-1))

                if ((i+1 < len(schematic)) and (j+1 < len(schematic[i])) and is_gear(schematic[i+1][j+1])):
                    is_adj_to_gears.add((i+1,j+1))

                if ((j-1 >= 0) and (i+1 < len(schematic)) and is_gear(schematic[i+1][j-1])):
                    is_adj_to_gears.add((i+1,j-1))

                if ((i-1 >= 0) and (j+1 < len(schematic[i])) and is_gear(schematic[i-1][j+1])):
                    is_adj_to_gears.add((i-1,j+1))
            else:
                if len(digits) > 0 and len(is_adj_to_gears) > 0:
                    for gear in is_adj_to_gears:
                        gears[gear].append(int("".join(digits)))
                digits = []
                is_adj_to_gears = set()


        if len(digits) > 0 and len(is_adj_to_gears) > 0:
            for gear in is_adj_to_gears:
                gears[gear].append(int("".join(digits)))

    ret = 0
    for k, v in gears.items():
        if len(v) == 2:
            ret += v[0] * v[1]

    return ret

if __name__ == "__main__":
    main_part_two()
