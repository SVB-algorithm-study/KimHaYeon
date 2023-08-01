class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        l = len(nums) / 2
        for i in nums:
            try:
                dic[i] += 1
                if dic[i] > l:
                    return i
            except:
                dic[i] = 1
        return nums[0]    
