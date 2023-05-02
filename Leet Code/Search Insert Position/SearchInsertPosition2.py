
class Solution(object):

    def BS(self, nums, low, high, target):
        mid = (low + high) // 2
        if nums[mid] >= target:
            if nums[mid-1] < target:
                return mid
            return self.BS(nums, low, mid, target)
        else:
            if nums[mid+1] >= target:
                return mid+1
            return self.BS(nums, mid, high, target)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums[0] >= target : 
            return 0
        elif nums[-1] < target:
            return len(nums)
        else:
            low = 0
            high = len(nums)-1
            return self.BS(nums, low, high, target)
