class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        rows = len(matrix)
        
        if not matrix:
            return False
        def binarysearch(row):
            l,r =0,col-1
            
            while l <= r:
                mid = (l+r)//2
                
                if matrix[row][mid]==target:
                    return True
                elif matrix[row][mid] < target:
                    l = mid+1
                else:
                    r = mid-1
                    
            return False
        
        for row in range(rows):
            if binarysearch(row):
                return True
        return False
                
                
           
        