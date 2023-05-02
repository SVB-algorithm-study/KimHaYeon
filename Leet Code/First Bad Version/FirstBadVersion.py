# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def BS(self, low, high):
        if low <= high :
            mid = (low + high) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else:
                    return self.BS(low,mid-1)
            else:
                return self.BS(mid+1, high)
        else:
            return -1
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        return self.BS(low, high)
