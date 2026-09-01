class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxl=height[l]
        maxr=height[r]
        water=0
        while l<r:
            if maxl<maxr:
                l+=1
                if maxl-height[l] >0:
                    water+=maxl-height[l]
                maxl=max(maxl,height[l])

            else:
                r-=1
                if maxr-height[r] >0:
                    water+=maxr-height[r]
                maxr=max(maxr,height[r])

        return water

        
