class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        prefix = [[0]*(col + 1) for r in range(row + 1)]
        
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                prefix[r][c] = prefix[r - 1][c]  + prefix[r][c - 1] - prefix[r - 1][c - 1] + matrix[r - 1][c - 1]
        
        count = 0
        for rStart in range(1, row + 1):
            for rEnd in range(rStart, row + 1):
                prevSum = {0: 1} # sum: count
                for c in range(1, col + 1):
                    Sum = prefix[rEnd][c] - prefix[rStart - 1][c]
                    if (Sum - target) in prevSum:
                        count += prevSum[Sum - target]
                    prevSum[Sum] = prevSum.get(Sum, 0) + 1
                    
        return count