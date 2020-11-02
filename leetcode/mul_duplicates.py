from typing import List

def findDuplicates(nums: List[int]) -> List[int]:
    ret = []
    for i in range(len(nums)):
        index = nums[i] - 1
        breakpoint()
        if nums[index] < 0:
            ret.append(abs(nums[i]))
        else:
            nums[index] *= -1
    return ret

findDuplicates([2, 2])
