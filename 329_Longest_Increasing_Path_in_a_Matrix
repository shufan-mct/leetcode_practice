class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dic = {} # start position: maxL
        
        def DFS(i, j, matrix, row, col, move, dic):
            if (i, j) in dic:
                return dic[(i,j)]
            maxL_ij = 1
            for di, dj in move:
                pi = i + di
                pj = j + dj
                if 0 <= pi < row and 0 <= pj < col and matrix[pi][pj] < matrix[i][j]:
                    maxL_ij = max(maxL_ij, DFS(pi, pj, matrix, row, col, move, dic) + 1)
            dic[(i, j)] = maxL_ij
            return maxL_ij
            
        maxL_all = 1
        for i in range(row):
            for j in range(col):
                maxL_all = max(maxL_all, DFS(i, j, matrix, row, col, move, dic))
                
        return maxL_all
