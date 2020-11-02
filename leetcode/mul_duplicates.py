from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                ret.append(abs(nums[i]))
            else:
                nums[index] *= -1
        return ret

Solution().findDuplicates([2, 2])
