def main():
    with open("input", "r") as f:
        lines = f.read().splitlines()

    ret = 0
    for l in lines:
        ret += get_calibration_number(l)

    print(ret)

def get_calibration_number(line: str) -> int:
    digits = [l for l in line if ord(l) >= ord('0') and ord(l) <= ord('9')]
    return int(digits[0] + digits[-1])

def run_tests():
    assert get_calibration_number("1abc2") == 12
    assert get_calibration_number("pqr3stu8vwx") == 38
    assert get_calibration_number("a1b2c3d4e5f") == 15
    assert get_calibration_number("treb7uchet") == 77

if __name__ == "__main__":
    main()
