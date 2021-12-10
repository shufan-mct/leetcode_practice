class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        neighbors = {i:set() for i in range(n)}
        for start, end in roads:
            neighbors[start].add(end)
            neighbors[end].add(start)      
        maxRank = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                rank = len(neighbors[i]) + len(neighbors[j])
                if j in neighbors[i]:
                    rank -= 1
                maxRank = max(rank, maxRank)
                if maxRank == 2 * n - 3:
                    return maxRank
        return maxRank
