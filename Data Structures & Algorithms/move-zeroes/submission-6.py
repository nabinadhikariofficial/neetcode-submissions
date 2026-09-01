class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        r=0
        l=0
        while (r<len(nums)):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            r+=1
        return