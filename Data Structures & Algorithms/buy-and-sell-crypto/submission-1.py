class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        ma=0
        while r<len(prices):
            if prices[l]<prices[r]:
                ma=max(prices[r]-prices[l],ma)                
            else:
                l=r
            r+=1
        return ma