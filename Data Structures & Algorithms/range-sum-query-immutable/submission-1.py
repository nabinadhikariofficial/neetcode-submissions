class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.prefix_sum=[nums[0]]*len(nums)
        for i in range(1,len(nums)):
            self.prefix_sum[i]=self.prefix_sum[i-1]+nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        sum=self.prefix_sum[right]-self.prefix_sum[left]+self.nums[left]
        return sum

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

