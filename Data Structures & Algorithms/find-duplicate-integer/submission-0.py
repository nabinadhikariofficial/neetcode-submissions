class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        value=set()

        for i in range(len(nums)):
            if nums[i] in value:
                return nums[i]
            value.add(nums[i])