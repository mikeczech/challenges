import math
from itertools import product


_x = 0
_y = 1

def eucl_dist(pos_a, pos_b):
    return math.sqrt((pos_a[_x] - pos_b[_x]) ** 2 + (pos_a[_y] - pos_b[_y]) ** 2)

def angle(pos_a, pos_b):
    return math.atan2(pos_a[_y] - pos_b[_y], pos_a[_x] - pos_b[_x])

def compute_all_pos(position, distance, dimensions):
    mirrored_pos = (set(), set())
    for d in [_x, _y]:
        k_max = int(math.floor(distance // ( 2 * dimensions[d]))) + 2
        for k in range(k_max):
            mirrored_pos[d].add(position[d] + k * 2 * dimensions[d])
            mirrored_pos[d].add(position[d] - 2 * position[d] + k * 2 * dimensions[d])
            mirrored_pos[d].add(position[d] - k * 2 * dimensions[d])
            mirrored_pos[d].add(position[d] - 2 * position[d] - k * 2 * dimensions[d])
    return product(*mirrored_pos)


def solution(dimensions, your_position, guard_position, distance):
    all_guard_pos = set(compute_all_pos(guard_position, distance, dimensions))
    all_your_pos = set(compute_all_pos(your_position, distance, dimensions))
    distances = {}
    targets = {}
    for p in all_guard_pos | all_your_pos:
        a = angle(your_position, p)
        d = eucl_dist(your_position, p)
        if d <= distance:
            if a not in distances or (a in distances and d < distances[a]):
                distances[a] = d
                targets[a] = p

    return len([p for p in targets.values() if p in all_guard_pos])


def assert_equals(value, expected):
    try:
        assert value == expected
    except AssertionError:
        print("{} != {}".format(value, expected))
        assert False


def run_tests():
    assert_equals(solution([3, 2], [1, 1], [2, 1], 4), 7)
    assert_equals(solution([300, 275], [150, 150], [185, 100], 500), 9)
    assert_equals(solution([2, 5], [1, 2], [1, 4], 11), 27)
    assert_equals(solution([23, 10], [6, 4], [3, 3], 5000), 329939)


run_tests()
