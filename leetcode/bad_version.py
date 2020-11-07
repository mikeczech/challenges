# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

import math

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        left = 0
        right = n
        while True:
            version = math.ceil((left + right) / 2)
            prev_version = version - 1
            if isBadVersion(version) and not isBadVersion(prev_version):
                return version

            if isBadVersion(version):
                right = version - 1
            else:
                left = version + 1
