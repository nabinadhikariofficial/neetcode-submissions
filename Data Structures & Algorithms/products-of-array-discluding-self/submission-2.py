class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1] * len(nums)
        # postfix = [1] * len(nums)
        pre=1
        post=1
        output=[1]* len(nums)
        # prefix[0]=nums[0]
        # postfix[-1]=nums[-1]
        for i in range(len(nums)):
            output[i]=pre
            pre *=nums[i]
        for i in range(len(nums)-1,-1,-1):
            output[i]*=post
            post *=nums[i]
        # output[0]=postfix[1]
        # output[-1]=prefix[-2]
        # print(prefix,postfix)
        # for i in range(len(nums)):
        #     output[i]=prefix[i]*postfix[i]
        return output
        