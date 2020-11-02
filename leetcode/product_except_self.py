from functools import reduce
import operator

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = {0: 1}
        r = {len(nums) - 1: 1}
        for i, n in enumerate(nums):
            l[i + 1] = l[i] * n
        for i, n in enumerate(nums[::-1]):
            r[len(nums) - i - 2] = r[len(nums) - i - 1] * n
        ret = []
        for i, n in enumerate(nums):
            ret.append(l[i] * r[i])
        return ret
