class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        output=[1]* len(nums)
        prefix[0]=nums[0]
        postfix[-1]=nums[-1]
        for i in range(1,len(nums)):
            prefix[i]=nums[i]*prefix[i-1]
        for i in range(len(nums)-2,0,-1):
            postfix[i]=nums[i]*postfix[i+1]
        output[0]=postfix[1]
        output[-1]=prefix[-2]
        for i in range(1,len(nums)-1):
            output[i]=prefix[i-1]*postfix[i+1]
        return output
        