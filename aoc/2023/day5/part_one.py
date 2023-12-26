import re
from collections import defaultdict

def main():
    with open("input", "r") as f:
        input_map = f.read()

    seeds, dicts = parse_map(input_map)
    location = determine_closest_location(seeds, dicts)


def run_tests():
    input_map = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
    """

    seeds, dicts = parse_map(input_map)
    location = determine_closest_location(seeds, dicts)

    print(location)
    assert location == 35


class OffsetDict:

    def __init__(self, src: int, dst: int, range_length: int):
        self.src = src
        self.dst = dst
        self.range_length = range_length

    def get(self, i: int):
        if i >= self.src and i <= self.src + self.range_length:
            return self.dst + (i - self.src)
        else:
            return None


def determine_closest_location(seeds, dicts):
    locations = []

    for s in seeds:
        target = s
        for d in dicts: # TODO refactor this
            match = None
            for dd in d:
                match = dd.get(target)
                if match:
                    break
            if not match:
                match = target
            target = match

        locations.append(target)

    return min(locations)


def parse_map(input_map: str, part_2: bool = False):
    seeds = [int(s) for s in re.search("seeds: ((\d+\s?)+)", input_map).group(1).split(" ")]

    dictionaries = []
    matches = re.finditer("(\w+)-to-(\w+) map:\n((\d+\s?)+)", input_map)
    for match in matches:
        dictionaries.append([])
        for l in match.group(3).split("\n"):
            numbers = [int(x.strip()) for x in l.split(" ") if x != '']
            if len(numbers) > 0:
                dst, src, length = numbers
                d = OffsetDict(src, dst, length)
                dictionaries[-1].append(d)

    return seeds, dictionaries


if __name__ == "__main__":
    run_tests()
