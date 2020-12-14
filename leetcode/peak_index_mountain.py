import math
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while True:
            i = math.floor((left + right) / 2)
            print(i)
            breakpoint()
            if arr[i-1] < arr[i] < arr[i + i]: # left side
                left = i + 1

            if arr[i-1] > arr[i] > arr[i + i]: # right side
                right = i - 1

            if arr[i-1] < arr[i] > arr[i + i]: # hurray! we found the peak
                return i

Solution().peakIndexInMountainArray([3,4,5,1])
