def main():
    with open("input", "r") as f:
        input_lines = f.read().splitlines()
    history = parse_history(input_lines)
    next_values = [predict_next_value_part_two(seq) for seq in history]
    print(sum(next_values))

def run_tests():
    input_lines = [
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45",
    ]

    history = parse_history(input_lines)
    # next_values = [predict_next_value(seq) for seq in history]
    # assert sum(next_values) == 114

    next_values = [predict_next_value_part_two(seq) for seq in history]
    assert sum(next_values) == 2

def parse_history(input_lines):
    return [[int(s) for s in l.split(" ")] for l in input_lines]

def compute_diff(seq):
    diff = []
    for i in range(1, len(seq)):
        diff.append(seq[i] - seq[i-1])
    return diff

def predict_next_value(seq):
    diffs = [seq]
    while any([i != 0 for i in diffs[-1]]):
        diffs.append(compute_diff(diffs[-1]))

    diffs[-1].append(0)
    for i in reversed(range(1, len(diffs))):
        last = diffs[i][-1]
        prev = diffs[i-1][-1]
        diffs[i-1].append(last + prev)

    return diffs[0][-1]

def predict_next_value_part_two(seq):
    diffs = [seq]
    while any([i != 0 for i in diffs[-1]]):
        diffs.append(compute_diff(diffs[-1]))

    diffs[-1].insert(0, 0)
    for i in reversed(range(1, len(diffs))):
        last = diffs[i][0]
        prev = diffs[i-1][0]
        diffs[i-1].insert(0, prev - last)

    return diffs[0][0]


if __name__ == "__main__":
    main()
