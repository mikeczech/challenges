import math
from typing import List
from collections import defaultdict

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        ret = set()
        for n_a in m:
            m[n_a] -= 1
            for n_b in m:
                if m[n_b] > 0:
                    m[n_b] -= 1
                    n_c = - n_a - n_b
                    if n_c in m and m[n_c] > 0:
                        ret.add(tuple(sorted([n_a, n_b, n_c])))
                    m[n_b] += 1
            m[n_a] += 1

        return ret

print(Solution().threeSum([0, 1, 1]))
