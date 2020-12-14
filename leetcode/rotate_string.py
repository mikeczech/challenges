class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        N = len(A)
        M = len(B)
        if N != M:
            return False

        breakpoint()
        return B in 2 * A,

assert not Solution().rotateString("abcde", "abced")
