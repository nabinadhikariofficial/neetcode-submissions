class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones= [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a=heapq.heappop(stones)
            b=heapq.heappop(stones)
            if a*-1 > b*-1:
                heapq.heappush(stones,(b-a)*-1)
            elif a*-1 < b*-1:
                heapq.heappush(stones,(a-b)*-1)
        if stones:
            return stones[0] *-1
        
        return 0