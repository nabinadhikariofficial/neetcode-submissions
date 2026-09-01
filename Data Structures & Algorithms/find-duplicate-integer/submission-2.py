class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # value=set()

        # for i in range(len(nums)):
        #     if nums[i] in value:
        #         return nums[i]
        #     value.add(nums[i])

        # value=0
        # for i in range(len(nums)-1):
        #     value=value ^ i+1

        # for i in range(len(nums)):
        #     value=value ^ nums[i]
        # return value

        slow,fast =0,0

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow == slow2:
                return slow