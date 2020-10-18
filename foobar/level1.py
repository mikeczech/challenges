import timeit

def solution(data, n):
    if len(data) > 99:
        raise ValueError()

    counts = {}
    for i in data:
        if i not in counts:
            counts[i] = 0
        counts[i] = counts[i] + 1

    return [i for i in data if counts[i] <= n]

def assert_equals(value, expected):
    try:
        assert value == expected
    except AssertionError:
        print("{} != {}".format(value, expected))

def run_tests():
    assert_equals(solution([1, 2, 3], 0), [])
    assert_equals(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1), [1, 4])
    assert_equals(solution([5, 10, 15, 10, 7], 1), [5, 15, 7])
    assert_equals(solution([1, 1, 1, 1, 1, 2], 5), [1, 1, 1, 1, 1, 2])
    assert_equals(solution([1, 1, 1, 1, 1, 2], 4), [2])
    assert_equals(solution([1, 1, 1, 1, 1, 2, 3, 3, 3, 9, 2, 2, 2, 3, 3, 3, 3], 5), [1, 1, 1, 1, 1, 2, 9, 2, 2, 2])
    assert_equals(solution([], 1), [])
    assert_equals(solution([1, 2, 3], -1), [])
    assert_equals(solution([1, -2, 3, 3], 1), [1, -2])

    try:
        solution([1] * 100, 2)
    except:
        assert True
    else:
        assert False

print(timeit.timeit(lambda: run_tests(), number=10000))
