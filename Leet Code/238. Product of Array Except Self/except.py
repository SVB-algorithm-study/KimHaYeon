class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] #앞에서부터 곱한 값 저장
        post = [1] # 뒤에서부터 곱한 값 저장
        result = [] # 결과 저장
        pre_num = 1
        post_num = 1
        
        for i in range(len(nums)):
            pre_num *= nums[i]
            pre.append(pre_num)
            
        for i in range(len(nums)-1,-1,-1):
            post_num *= nums[i]
            post.append(post_num)
            
        # print(pre, post)
        
        for i in range(len(nums)):
            result.append(pre[i] * post[len(nums)-i-1])
        
        return result
        
