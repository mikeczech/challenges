from collections import Counter
import operator

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return min(Counter(nums).items(), key=operator.itemgetter(1))[0]
