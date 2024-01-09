import re
from math import lcm
from collections import defaultdict

def main():
    with open("input", "r") as f:
        input_network = [l for l in f.read().splitlines() if l != '']
    instr, network = parse_network(input_network)
    result = num_steps(instr, network)
    print(result)

def run_tests():
    input_network_a = [
        "LR",
        "",
        "11A = (11B, XXX)",
        "11B = (XXX, 11Z)",
        "11Z = (11B, XXX)",
        "22A = (22B, XXX)",
        "22B = (22C, 22C)",
        "22C = (22Z, 22Z)",
        "22Z = (22B, 22B)",
        "XXX = (XXX, XXX)",
    ]

    instr, network = parse_network(input_network_a)
    result = num_steps(instr, network)
    assert result == 6


def parse_network(input_network):
    instr = input_network[0]
    network = defaultdict(dict)

    input_network = input_network[1:]
    for i in input_network:
        match = re.search("([1-9A-Z]{3}) = \(([1-9A-Z]{3}), ([1-9A-Z]{3})\)", i)
        if match:
            network[match.group(1)]["L"] = match.group(2)
            network[match.group(1)]["R"] = match.group(3)

    return instr, network

def num_steps(instr, network):
    current = [n for n in network if n.endswith("A")]
    path_lengths = []

    for c in current:
        found = False
        num_steps = 0
        while not found:
            for i in instr:
                c = network[c][i]
                num_steps += 1
                if c.endswith("Z"):
                    found = True
                    break
        path_lengths.append(num_steps)

    return lcm(*path_lengths)


if __name__ == "__main__":
    main()
