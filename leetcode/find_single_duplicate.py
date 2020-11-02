class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        snums = sorted(nums)
        for i, n in enumerate(snums):
            if snums[i+1] == n:
                return n
