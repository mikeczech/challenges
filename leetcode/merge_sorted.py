class Solution:
    
    # A: 2 2 5 6 6 7 7 11 x x x x x
    #                             k
    #                   x       
    # B: 12 13 14 15
    # y
            
            
    # Apporach 1) Concatenate both arrays and sort. O(m + nlogn)
    # Apporach 2) Add every element from B into A and move it to the right place. O(n x n)  
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = m - 1
        y = n - 1
        k = m + n - 1
        
        while x >= 0 and y >= 0:
            if nums1[x] > nums2[y]:
                nums1[k] = nums1[x]
                x -= 1
                k -= 1
            else:
                nums1[k] = nums2[y]
                y -= 1
                k -= 1
        
        while y >= 0:
            nums1[k] = nums2[y]
            y -= 1
            k -= 1
