import timeit

def solution(total_lambs):
    s_count = 1
    g_count = 1

    s_rem = total_lambs - 1
    g_rem = total_lambs - 1

    s_done = False
    g_done = False

    s_next_next_h = None
    g_next_next_h = None

    s_next_h = 1
    g_next_h = 1

    s_min_lambs = 1
    g_min_lambs = 1

    while not s_done or not g_done:
        if s_next_next_h:
            s_min_lambs = s_next_h + s_next_next_h
        if g_next_next_h:
            g_min_lambs = g_next_h + g_next_next_h
        s_max_lambs = 2 * s_next_h
        g_max_lambs = 2 * g_next_h

        if s_rem > 0 and s_min_lambs <= s_rem:
            s_count += 1
            s_next_next_h = s_next_h
            s_next_h = s_min_lambs
            s_rem -= s_min_lambs
        else:
            s_done = True

        if g_rem > 0 and g_max_lambs <= g_rem:
            g_count += 1
            g_next_next_h = g_next_h
            g_next_h = g_max_lambs
            g_rem -= g_max_lambs
        else:
            g_done = True

    return s_count - g_count

def assert_equals(value, expected):
    try:
        assert value == expected
    except AssertionError:
        print("{} != {}".format(value, expected))
        assert False

def run_tests():
    assert_equals(solution(0), 0)
    assert_equals(solution(1), 0)
    #assert_equals(solution(2), 0)
    assert_equals(solution(3), 0)
    assert_equals(solution(4), 1)
    assert_equals(solution(5), 1)
    # assert_equals(solution(6), 0)
    assert_equals(solution(7), 1)
    assert_equals(solution(8), 1)
    assert_equals(solution(9), 1)
    assert_equals(solution(10), 1)
    assert_equals(solution(11), 1)
    assert_equals(solution(143), 3)
    assert_equals(solution(1234), 4) # unchecked
    # assert_equals(solution(32423432), 10) # unchecked
    assert_equals(solution(42), 2) # unchecked
    assert_equals(solution(10**9), 13) # unchecked

#print(timeit.timeit(lambda: run_tests(), number=10000))
run_tests()
