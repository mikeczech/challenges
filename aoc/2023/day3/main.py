from typing import List

def main():
    with open("input", "r") as f:
        schematic = f.read().splitlines()
    sum_ = part_number_sum(schematic)
    print(sum_)


def run_tests():
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

    sum_ = part_number_sum(schematic)

    assert sum_ == 4361


def is_number(c: str):
    return ord(c) >= 48 and ord(c) <= 57

def is_symbol(c: str):
    if ord(c) >= 48 and ord(c) <= 57:
        return False
    if c == ".":
        return False
    return True

def part_number_sum(schematic: List[str]):
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


if __name__ == "__main__":
    main()
