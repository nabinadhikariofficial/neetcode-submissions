class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum=sum(nums)
        lsum=0
        for i in range(len(nums)):
            if rsum-nums[i]==lsum:
                return i
            rsum-=nums[i]
            lsum+=nums[i]
        return -1 
        