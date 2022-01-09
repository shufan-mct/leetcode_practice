class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        
        for i in range(n):
            set1 = set([i for i in range(1, n + 1)])
            set2 = set([i for i in range(1, n + 1)])
            for j in range(n):
                if matrix[i][j] in set1:
                    set1.remove(matrix[i][j])
                else:
                    return False
                if matrix[j][i] in set2:
                    set2.remove(matrix[j][i])
                else:
                    return False
            
        return True