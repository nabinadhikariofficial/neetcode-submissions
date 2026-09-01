class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        heapq.heapify(h)
        res=[]
        for point in points:
            distance=point[0] ** 2 + point[1] **2
            heapq.heappush(h,[distance,point])
        
        while k>0:
            point=heapq.heappop(h)
            print(point)
            res.append([point[1][0],point[1][1]])
            k-=1
        
        return res
