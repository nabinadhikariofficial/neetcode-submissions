class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum={0:1}
        res=0
        sum=0

        for i in range(len(nums)):
            sum+=nums[i]
            diff=sum-k
            res+=prefixSum.get(diff,0)
            prefixSum[sum]=1+prefixSum.get(sum,0)
        
        return res

            