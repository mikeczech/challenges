import math
from typing import List

class Solution:
    def contains(self, value, snums):
        l = 0
        r = len(snums) - 1
        while l <= r:
            mid = math.floor((l + r) / 2)
            if snums[mid] == value:
                return True
            if snums[mid] > value:
                r =  mid - 1
            else:
                l = mid + 1
        return False

    def twoSum(self, n_a: int,  nums: List[int], cache) -> List[List[int]]:
        if len(nums) < 2:
            return []
        ret = []
        for i, n_b in enumerate(nums):
            key = tuple(sorted([n_a, n_b]))
            if key not in cache: 
                n_c = - n_a - n_b
                if self.contains(n_c, nums[:i] + nums[i+1:]):
                    ret.append(tuple(sorted([n_a, n_b, n_c])))
                cache.add(key)
                
        return ret

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        cache = set()
        ret = set()
        for i, n_a in enumerate(nums):
            if n_a not in cache:
                two_sum_ret = self.twoSum(n_a, nums[:i] + nums[i+1:])
                for s in two_sum_ret:
                    ret.add(s)
                cache.add(n_a)
        return ret


print(Solution().threeSum([0, 1, 1]))
