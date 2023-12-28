import re

def main():
    with open("input", "r") as f:
        races_input = f.read()
    races = parse_races(races_input, part_2=True)
    print(races)
    num_ways = num_ways_to_beat_the_record(races)
    print(num_ways)


def run_tests():
    races_input = """
Time:      7  15   30
Distance:  9  40  200
    """

    races = parse_races(races_input)
    num_ways = num_ways_to_beat_the_record(races)

    assert num_ways == 288


def parse_races(races_input: str, part_2 = False):
    if part_2:
        races_input = races_input.replace(" ", "")
    times = [int(t.strip()) for t in re.search("Time:\s*((\d+\s*)+)", races_input).group(1).split(" ") if t != '']
    distances = [int(d.strip()) for d in re.search("Distance:\s*((\d+\s*)+)", races_input).group(1).split(" ") if d != '']

    return times, distances

def num_ways_to_beat_the_record(races):
    times, distances = races
    ret = 1
    for t, record_distance in zip(times, distances):
        num_ways = 0
        for i in range(t):
            distance = determine_distance(i, t)
            if distance > record_distance:
                num_ways += 1
        ret *= max(num_ways, 1)
    return ret

def determine_distance(hold_milli: int, race_time_milli: int):
    if hold_milli == 0:
        return 0
    return (race_time_milli - hold_milli) * hold_milli


if __name__ == "__main__":
    main()
