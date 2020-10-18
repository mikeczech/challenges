import timeit
import time
import pdb
from collections import deque

NO_SOLUTION = -1

class Location:
    def __init__(self, x, y, taint=False):
        self.x = x
        self.y = y
        self.taint = taint

    def __hash__(self):
        return hash((self.x, self.y, self.taint))

    def __eq__(self, other):
        return other and self.x == other.x and self.y == other.y and self.taint == other.taint


def get_adjacent(map, current_loc, w, h):
    candidates = set()
    x = current_loc.x
    y = current_loc.y
    taint = current_loc.taint
    if x + 1 < w:
        candidates.add(Location(x+1, y, taint or map[y][x+1] == 1))
    if x - 1 >= 0:
        candidates.add(Location(x-1, y, taint or map[y][x-1] == 1))
    if y + 1 < h:
        candidates.add(Location(x, y + 1, taint or map[y+1][x] == 1))
    if y - 1 >= 0:
        candidates.add(Location(x, y - 1, taint or map[y-1][x] == 1))

    return {c for c in candidates if map[c.y][c.x] == 0 or not taint}


def solution(map):
    w = len(map[0])
    h = len(map)

    assert 2 <= w <= 20
    assert 2 <= h <= 20

    start = Location(0, 0)
    parent = {start: start}
    queue = deque()
    queue.append(start)
    distance = {start: 1}

    while len(queue) > 0:
        current = queue.popleft()
        if (current.x, current.y) == (w-1, h-1):
            return distance[current]

        adjacent_locs = get_adjacent(map, current, w, h)
        for n in adjacent_locs:
            if n not in parent:
                parent[n] = current
                distance[n] = distance[current] + 1
                queue.append(n)

    return NO_SOLUTION


def assert_equals(value, expected):
    try:
        assert value == expected
    except AssertionError:
        print("{} != {}".format(value, expected))
        assert False

def run_tests():
    assert_equals(solution([[0, 1], [1, 0]]), 3)
    assert_equals(solution([[0, 1], [0, 0]]), 3)
    assert_equals(solution([[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0], [0, 1, 1, 0]]), 8)
    assert_equals(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]), 7)
    assert_equals(solution([[0] * 20] * 20), 39)
    assert_equals(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]), 11)
    assert_equals(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]]), 13)
    assert_equals(solution([[0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 1, 1 ,1 ,1], [0, 0, 0, 0 ,0 ,0 ,0]]), 13)
    matrix = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
               [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert_equals(solution(matrix), 39)
    assert_equals(solution([[0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0]]), 11)


#print(timeit.timeit(lambda: run_tests(), number=3))
run_tests()


def test_solution():
    assert solution([
        [0, 1, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 1, 1], 
        [0, 1, 1, 0],
        [0, 1, 1, 0]
    ]) == 8

    assert solution([
        [0, 1, 0, 0, 0], 
        [0, 0, 0, 1, 0], 
        [0, 0, 1, 1, 0], 
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ]) == 9

    # assert solution([
    #     [0, 1, 0, 0, 0], 
    #     [0, 0, 0, 1, 0], 
    #     [0, 0, 1, 1, 1], 
    #     [0, 1, 1, 0, 0],
    #     [0, 1, 1, 0, 0]
    # ]) == 11

    # assert solution([
    #     [0, 1, 0, 0, 0], 
    #     [0, 1, 0, 1, 0], 
    #     [0, 0, 0, 1, 0], 
    #     [0, 0, 1, 1, 1], 
    #     [0, 1, 1, 0, 0],
    #     [0, 1, 1, 0, 0]
    # ]) == 14

    # assert solution([
    #     [0, 1, 0, 0, 0], 
    #     [0, 1, 0, 1, 0], 
    #     [0, 0, 0, 1, 0], 
    #     [0, 1, 1, 1, 1],
    #     [0, 1, 1, 1, 0]
    # ]) == 13

    assert solution([
        [0, 1, 1, 0], 
        [0, 0, 0, 1], 
        [1, 1, 0, 0], 
        [1, 1, 1, 0]
    ]) == 7

    assert solution([
        [0, 0, 0, 0, 0, 0], 
        [1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1], 
        [0, 1, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0]
    ]) == 11

    assert solution([
        [0, 0],
        [0, 0]
    ]) == 3

    assert solution([
        [0, 0],
        [0, 1]
    ]) == 3

#test_solution()
