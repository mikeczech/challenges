import operator

class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache = set(s)
        for j in range(0, len(s) - 2 + 1):
            subs = s[j:j+2]
            if subs[0] == subs[-1]:
                cache.add(subs)

        for i in range(3, len(s) + 1):
            for j in range(0, len(s) - i + 1):
                subs = s[j:j+i]
                if subs[0] == subs[-1] and subs[1:-1] in cache:
                    cache.add(subs)
        return max(cache, key=len)

assert Solution().longest_palindrom("babad") == "aba"
assert Solution().longest_palindrom("cbbd") == "bb"
assert Solution().longest_palindrom("aba") == "aba"
assert Solution().longest_palindrom("ccc") == "ccc"
