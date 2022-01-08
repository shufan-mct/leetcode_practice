class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        dp = {} # positions of two robots: max collection from here to bottom
        
        def DP(row, col1, col2, dp, r, c, grid):
            if col1 < 0 or col1 >= c or col2 < 0 or col2 >= c:
                return -float('inf')
                            
            if col2 < col1:
                return DP(row, col2, col2, dp, r, c, grid)
            
            if (row, col1, col2) in dp:
                return dp[(row, col1, col2)]
            
            if col1 == col2:
                curr = grid[row][col1]
            else:
                curr = grid[row][col1] + grid[row][col2]
                
            if row == r - 1:
                dp[(row, col1, col2)] = curr
                return curr
            
            future = 0
            for hmove1 in range(-1, 2):
                for hmove2 in range(-1, 2):
                    future = max(future, \
                                 DP(row + 1, col1 + hmove1, col2 + hmove2, dp, r, c, grid))
            dp[(row, col1, col2)] = curr + future
            
            return curr + future
        
        return DP(0, 0, c - 1, dp, r, c, grid)