class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max=0
        while l<r:
            width=r-l
            if heights[l]>heights[r]:
                area=heights[r]*width
                r-=1
            else:
                area=heights[l]*width
                l+=1
            if area>max:
                max=area
        return max