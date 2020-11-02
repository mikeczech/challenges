class Solution:
    INT_MAX = 2**31
    INT_MIN = -2**31 - 1

    def reverse(self, x: int) -> int:
        if x < 0:
            neg = True
            x *= -1
        else:
            neg = False
        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10
            rev = rev * 10 + pop
        if rev > self.INT_MAX or rev < self.INT_MIN:
            return 0
        return rev if not neg else -rev
