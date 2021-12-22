class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0]) 
        adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def DFS(n, i, j, row, col, grid, adj):
            grid[i][j] = n
            area = 1
            for di, dj in adj:
                ni, nj = i + di, j + dj
                if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 1:
                    area += DFS(n, ni, nj, row, col, grid, adj)
            return area
        
        maxA = 0
        areas = {} # island code: area
        n = 2
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    areas[n] = DFS(n, i, j, row, col, grid, adj)
                    maxA = max(maxA, areas[n])
                    n += 1
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    area = 1
                    neighbor = set()
                    for di, dj in adj:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] >= 2 and \
                        grid[ni][nj] not in neighbor:
                            area += areas[grid[ni][nj]]
                            neighbor.add(grid[ni][nj])
                    maxA = max(maxA, area)
        return maxA