import re
from collections import defaultdict

def main():
    with open("input", "r") as f:
        input_network = [l for l in f.read().splitlines() if l != '']
    instr, network = parse_network(input_network)
    result = num_steps(instr, network)
    print(result)

def run_tests():
    input_network_a = [
        "RL",
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)"
    ]

    instr, network = parse_network(input_network_a)
    result = num_steps(instr, network)
    assert result == 2

    input_network_b = [
        "LLR",
        "AAA = (BBB, BBB)",
        "BBB = (AAA, ZZZ)",
        "ZZZ = (ZZZ, ZZZ)"
    ]

    instr, network = parse_network(input_network_b)
    result = num_steps(instr, network)
    assert result == 6



def parse_network(input_network):
    instr = input_network[0]
    network = defaultdict(dict)

    input_network = input_network[1:]
    for i in input_network:
        match = re.search("([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", i)
        network[match.group(1)]["L"] = match.group(2)
        network[match.group(1)]["R"] = match.group(3)

    return instr, network

def num_steps(instr, network):
    current = "AAA"
    num_steps = 0

    found = False
    while not found:
        for i in instr:
            current = network[current][i]
            num_steps += 1
            if current == "ZZZ":
                found = True

    return num_steps


if __name__ == "__main__":
    main()
