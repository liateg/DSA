class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        if n==1 or m==1:
            return True
        j=0
        i=0
        while j<n-1 and i<m-1:
            if matrix[i][j]!=matrix[i+1][j+1]:
                return False
            j+=1

        for i in range(m):
            j=0
            while j<n-1 and i<m-1:
                if matrix[i][j]!=matrix[i+1][j+1]:
                    
                    return False
                j+=1

        return True