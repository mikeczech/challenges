import timeit
import pdb

def count_codes(l, i, depth, cache):
    num_codes = 0
    for j in range(i + 1, len(l)):
        if l[j] % l[i] == 0:
            if depth < 2:
               if j in cache:
                  num_codes += cache[j]
               else:
                  num_codes += count_codes(l, j, depth + 1, cache)
            else:
               num_codes += 1

    cache[i] = num_codes
    return num_codes


def solution(l):
    cache = {}
    return sum([count_codes(l, i, 1, cache) for i in range(len(l))])


def assert_equals(value, expected):
    try:
        assert value == expected
    except AssertionError:
        print("{} != {}".format(value, expected))
        assert False

def run_tests():
    assert_equals(solution([1, 2, 3, 4, 5, 6]), 3)
    solution([1] * 2000)
    assert_equals(solution([1, 1, 1]), 1)
    assert_equals(solution([1, 3, 7]), 0)
    assert_equals(solution([1, 3]), 0)

print(timeit.timeit(lambda: run_tests(), number=3))
# run_tests()

