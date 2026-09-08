class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res=r

        def canShip(cap):
            ships,cuuCap=1,cap
            for w in weights:
                if cuuCap-w<0:
                    ships+=1
                    cuuCap=cap
                cuuCap-=w
            return ships<=days

        while l<=r:
            cap=l+((r-l)//2)
            if canShip(cap):
                res=min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res