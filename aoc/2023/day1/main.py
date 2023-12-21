def main():
    with open("input", "r") as f:
        lines = f.read().splitlines()

    ret = 0
    for l in lines:
        ret += get_calibration_number(l)

    print(ret)

def get_calibration_number(line: str) -> int:
    forward = Matcher()
    first_digit = None
    for c in line:
        first_digit = forward.add_char(c)
        if first_digit:
            break

    backward = Matcher()
    last_digit = None
    for c in line[::-1]:
        last_digit = backward.add_char(c, revert=True)
        if last_digit:
            break

    return int(str(first_digit) + str(last_digit))

class Matcher:

    def __init__(self):
        self.patterns = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

        self.pointers = [0] * len(self.patterns)

    def add_char(self, c: str, revert: bool = False):
        for i, p in enumerate(self.patterns.keys()):
            if revert:
                p = p[::-1]
            if p[self.pointers[i]] == c:
                if len(p[self.pointers[i] + 1:]) == 0:
                    if revert:
                        return self.patterns[p[::-1]]
                    else:
                        return self.patterns[p]
                else:
                    self.pointers[i] += 1
            else:
                self.pointers[i] += 0
        return None

def run_tests():
    assert get_calibration_number("1abc2") == 12
    assert get_calibration_number("pqr3stu8vwx") == 38
    assert get_calibration_number("a1b2c3d4e5f") == 15
    assert get_calibration_number("treb7uchet") == 77

    assert get_calibration_number("two1nine") == 29
    assert get_calibration_number("eightwothree") == 83
    assert get_calibration_number("abcone2threexyz") == 13
    assert get_calibration_number("xtwone3four") == 24
    assert get_calibration_number("4nineeightseven2") == 42
    assert get_calibration_number("zoneight234") == 14
    assert get_calibration_number("7pqrstsixteen") == 76

if __name__ == "__main__":
    main()
