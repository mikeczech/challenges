from collections import defaultdict

def has_unique(input_string): # no additional data structures
    input_string = sorted(input_string)
    N = len(input_string)
    if N == 0:
        return True
    for i in range(N - 1):
        if input_string[i] == input_string[i + 1]:
            return False
    return True

assert has_unique("fhiwnc") == True
assert has_unique("ffgeic") == False
assert has_unique("") == True
assert has_unique("a") == True

def is_permutation(str1, str2):
    return sorted(str1) == sorted(str2)

assert is_permutation("4136", "1614") == False

def assert_equal(expected, value):
    try:
        assert expected == value
    except:
        print(f"{expected} != {value}")

def replace_ws(input_string):
    input_string = list(input_string)
    N = len(input_string)
    for i in range(N - 2):
        if input_string[i] == ' ':
            for j in range(N - 3, i + 1, -1):
                input_string[j + 2] = input_string[j]
                input_string[j + 1] = input_string[j - 1]
            input_string[i] = '%'
            input_string[i+1] = '2'
            input_string[i+2] = '0'
    return "".join(input_string)

assert_equal("hello%20world", replace_ws("hello world  "))
assert_equal("hello%20world%20foo%20bar", replace_ws("hello world foo bar      "))

def compress(input_string):
    input_string += "\0"
    N = len(input_string)
    res = []
    count = 1
    c = input_string[0]
    for i in range(1, N):
        if input_string[i] == c:
            count += 1
        else:
            res.append(f"{c}{count}")
            c = input_string[i]
            count = 1

    res = "".join(res)
    if len(res) >= len(input_string[:-1]):
        return input_string[:-1]
    return res

assert_equal("a2b1c5a3", compress("aabcccccaaa"))
assert_equal("aabb", compress("aabb"))
