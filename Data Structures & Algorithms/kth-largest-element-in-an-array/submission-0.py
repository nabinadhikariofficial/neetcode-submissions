class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        heapq.heapify(h)
        for num in nums:
            heapq.heappush(h,num*-1)
        
        while k-1>0:
            heapq.heappop(h)
            k-=1

        return h[0]*-1
        