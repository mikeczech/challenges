import timeit
import pdb

def subtract(x, y, b):
    assert len(x) == len(y)

    carry = 0
    ret = []
    for i, j in zip(x[::-1], y[::-1]):
        sub = int(i) - int(j)
        val = (sub - carry) % b
        carry = 0 if (sub - carry) >= 0 else 1
        ret.append(str(val))

    assert carry == 0 # y < x

    return "".join(ret[::-1])


def solution(n, b):
    assert 2 <= b <= 10
    assert 2 <= len(n) <= 9

    current_pos = 0
    ids_pos = {n: current_pos}

    while True:
        x = "".join(sorted(n, reverse=True))
        y = x[::-1]
        z = subtract(x, y, b)
        if z in ids_pos: # hurray! we found a cycle!
            return (current_pos - ids_pos[z]) + 1
        else:
            current_pos += 1
            ids_pos[z] = current_pos
            n = z


def assert_equals(value, expected):
    try:
        assert value == expected
    except AssertionError:
        print("{} != {}".format(value, expected))
        assert False

def run_tests():
    assert_equals(subtract('1125', '0031', 10), '1094')
    assert_equals(subtract('2012', '0211', 3), '1101')
    assert_equals(subtract('2111', '1112', 10), '0999')
    assert_equals(subtract('9990', '0999', 10), '8991')
    assert_equals(subtract('1332', '1211', 4), '0121')
    assert_equals(subtract('2355', '1453', 6), '0502')

    assert_equals(solution('1211', 10), 1)
    assert_equals(solution('210022', 3), 3)
    assert_equals(solution('210022232', 3), 1)

# print(timeit.timeit(lambda: run_tests(), number=10000))
run_tests()

