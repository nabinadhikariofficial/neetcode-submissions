class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones= [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a=heapq.heappop(stones)
            b=heapq.heappop(stones)
            if b > a:
                heapq.heappush(stones,a-b)
        if stones:
            return stones[0] *-1
        
        return 0