class UnionFind:
    
    def __init__(self, size):
        self.parent = [i for i in range(size)]
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
            
        return self.parent[i]
    
    def union(self, i, j):
        par_i = self.find(i)
        par_j = self.find(j)
        
        if par_i == par_j:
            return False
        else:
            self.parent[par_i] = par_j
            return True
            

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        groups = n
        logs.sort()
        
        for (timeStamp, x, y) in logs:
            if uf.union(x, y):
                n -= 1
            if n == 1:
                return timeStamp
        return -1