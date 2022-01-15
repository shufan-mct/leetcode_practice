from queue import Queue

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        numToIdx = {} # arr:[idx]
        for i, num in enumerate(arr):
            if num not in numToIdx:
                numToIdx[num] = [i]
            else:
                numToIdx[num].append(i)
        
        visited = [0] * n
        valuesBeSeenAll = set()
        
        step = 0
        q = Queue()
        q.put(0)
        visited[0] = 1
        
        while not q.empty():
            step += 1
            levelLen = q.qsize()
            for i in range(levelLen):
                start = q.get()
                
                if start + 1 == n - 1:
                    return step
                elif visited[start + 1] == 0:
                    visited[start + 1] = 1
                    q.put(start + 1)
                    
                if start - 1 >= 0 and visited[start - 1] == 0:
                    visited[start - 1] = 1
                    q.put(start - 1)
                    
                if arr[start] not in valuesBeSeenAll:
                    for idx in numToIdx[arr[start]]:
                        if idx == n - 1:
                            return step
                        if visited[idx] == 0:
                            visited[idx] = 1
                            q.put(idx)
                    valuesBeSeenAll.add(arr[start])

        return -1