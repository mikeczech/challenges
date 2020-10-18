def count_trailing_zeroes(n):
    ret = 0
    while (n & 1) == 0:
        ret += 1
        n = n >> 1
    return ret

def solution(n):
    n = long(n)
    if n == 0:
        return 1
    ret = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        elif n == 3:
            n = 2
        else:
            n_incr_trailing_zeroes = count_trailing_zeroes(n + 1)
            n_decr_trailing_zeroes = count_trailing_zeroes(n - 1)
            if n_incr_trailing_zeroes > n_decr_trailing_zeroes:
                n = n + 1
            else:
                n = n - 1
        ret += 1

    return ret


def assert_equals(value, expected):
    try:
        assert value == expected
    except AssertionError:
        print("{} != {}".format(value, expected))
        assert False

def run_tests():
    assert Pellets("2").is_even()
    assert Pellets("42").is_even()
    assert not Pellets("73").is_even()
    assert Pellets("3" * 300 + "2").is_even()

    assert_equals(Pellets("2").incr(), "3")
    assert_equals(Pellets("9").incr(), "10")
    assert_equals(Pellets("15").incr(), "16")
    assert_equals(Pellets("19").incr(), "20")
    assert_equals(Pellets("299").incr(), "300")

    assert_equals(Pellets("2").decr(), "1")
    assert_equals(Pellets("15").decr(), "14")
    assert_equals(Pellets("10").decr(), "9")
    assert_equals(Pellets("20").decr(), "19")
    assert_equals(Pellets("300").decr(), "299")

    assert_equals(Pellets("8").divide(), "4")
    assert_equals(Pellets("16").divide(), "8")
    assert_equals(Pellets("26").divide(), "13")
    assert_equals(Pellets("34").divide(), "17")
    assert_equals(Pellets("300").divide(), "150")
    assert_equals(Pellets("350").divide(), "175")

    assert_equals(solution("0"), 1)
    assert_equals(solution("1"), 0)
    assert_equals(solution("2"), 1)
    assert_equals(solution("3"), 2)
    assert_equals(solution("16"), 4)
    assert_equals(solution("15"), 5)
    assert_equals(solution("4"), 2)

run_tests()
