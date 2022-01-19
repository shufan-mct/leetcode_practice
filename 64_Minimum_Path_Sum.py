class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        minCost = [[0] * col for i in range(row)]
        
        minCost[0][0] = grid[0][0]
        for r in range(1, row):
            minCost[r][0] = minCost[r - 1][0] + grid[r][0]
        for c in range(1, col):
            minCost[0][c] = minCost[0][c - 1] + grid[0][c]        
            
        for r in range(1, row):
            for c in range(1, col):
                minCost[r][c] = min(minCost[r - 1][c], minCost[r][c - 1]) + grid[r][c]
                
        return minCost[row - 1][col - 1]