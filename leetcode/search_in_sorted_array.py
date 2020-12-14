import math
from typing import List

#  4 5 6 7 
#  p   m

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p = nums[0]
        q = nums[-1]
        if p == target:
            return 0
        if q == target:
            return len(nums) - 1
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] != target:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = math.floor((left + right) / 2)
            print(f"Left: {nums[left]} [{left}]")
            print(f"Right: {nums[right]} [{right}]")
            print(nums[mid])
            breakpoint()

            if nums[mid] > nums[mid+1]:
                break
            if nums[mid] < nums[mid-1]:
                mid -= 1
                break
            if nums[mid] == target:
                return mid

            if nums[mid] >= p and nums[mid] > q: # left
                left = mid + 1
            else: # right
                right = mid - 1

        rotation_point = mid
        if target >= p and target > q:
            left = 0
            right = rotation_point
        else:
            right = len(nums) - 1
            left = rotation_point + 1

        while left <= right:
            mid = math.floor((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


assert Solution().search([4,5,6,7,8,1,2,3], 8) == 4
