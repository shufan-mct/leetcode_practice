class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbors = {} # node values: set()
        for u, v in adjacentPairs:
            if u not in neighbors:
                neighbors[u] = set()
            neighbors[u].add(v)
            if v not in neighbors:
                neighbors[v] = set()
            neighbors[v].add(u)
        
        for node in neighbors:
            if len(neighbors[node]) == 1:
                break
                
        restored = []
        seen = set()
                
        while True:
            restored.append(node)
            seen.add(node)
            can = neighbors[node].pop()
            if can not in seen:
                node = can
            else:
                if len(neighbors[node]) == 0:
                    break
                else:
                    node = neighbors[node].pop()
        
        return restored