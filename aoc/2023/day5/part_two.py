import re
from collections import defaultdict

import numpy as np
from numba import njit, jit

def main():
    with open("input", "r") as f:
        input_map = f.read()

    seed_pars, stages = parse_map(input_map)
    location = determine_closest_location(seed_pairs, stages)


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

    seed_pairs, stages = parse_map(input_map)
    location = determine_closest_location(seed_pairs, stages)

    assert location == 46

def parse_map(input_map: str):
    seeds = [int(s) for s in re.search("seeds: ((\d+\s?)+)", input_map).group(1).split(" ")]
    seed_pairs = []
    for i in range(1, len(seeds), 2):
        seed_pairs.append((seeds[i - 1], seeds[i]))

    stages = []
    matches = re.finditer("(\w+)-to-(\w+) map:\n((\d+\s?)+)", input_map)
    for match in matches:
        stages.append([])
        for l in match.group(3).split("\n"):
            numbers = [int(x.strip()) for x in l.split(" ") if x != '']
            if len(numbers) > 0:
                dst, src, length = numbers
                stages[-1].append((src, dst, length))

    max_stage_len = max([len(stage) for stage in stages])
    for stage in stages:
        while len(stage) < max_stage_len:
            stage.append((-1, -1, -1))

    return np.array(seed_pairs), np.array(stages)


@njit(parallel=True)
def determine_closest_location(seed_pairs, stages):
    min_location = np.inf
    for pair in seed_pairs:
        seeds = np.arange(pair[0], pair[0] + pair[1] + 1)
        transformed = seeds
        for stage in stages:
            not_yet_mapped = np.full(transformed.shape[0], True)
            for t in stage:
                condition = (transformed >= t[0]) & (transformed < t[0] + t[2]) & not_yet_mapped
                transformed = np.where(condition, t[1] + (transformed - t[0]), transformed)
                not_yet_mapped = np.where(condition, False, not_yet_mapped)
        min_location = min(np.min(transformed), min_location)
    return min_location


if __name__ == "__main__":
    run_tests()
