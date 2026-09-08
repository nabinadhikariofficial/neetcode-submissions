class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        l=0
        r=row*col- 1
        while l<=r:
            m=l+((r-l)//2)
            res=matrix[m//col][m % col]
            if res==target:
                return True
            elif res> target:
                r=m-1
            else:
                l=m+1
        return False

        