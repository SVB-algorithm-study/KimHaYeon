class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        # Reverse the entire list
        nums[:] = nums[::-1]
        
        # Reverse the first k elements
        nums[:k] = nums[:k][::-1]
        
        # Reverse the remaining n - k elements
        nums[k:] = nums[k:][::-1]
