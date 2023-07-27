class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tmp = 1
        num = nums[-1]
        flag = False
        if len(nums) < 2:
            return True
        if nums[0] == 0:
            return False
        for i in range(len(nums)-2, -1, -1):
            # print(tmp, num)
            num = nums[i]
            if tmp > num:
                tmp += 1
                flag = False
            else:
                tmp = 1
                flag = True
        return flag
               
