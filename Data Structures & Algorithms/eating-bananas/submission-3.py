class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=max(piles)
        while l<=r:
            m=l+((r-l)//2)

            hour=0
            for b in piles:
                hour+=(-(-b//m))
            if hour<=h:
                res=min(res,m)
                r=m-1
            else:
                l=m+1
        return res
        