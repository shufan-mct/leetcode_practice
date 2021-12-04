from queue import Queue

class Solution:
    def alienOrder(self, words: List[str]) -> str:        
        letters = set()
        for word in words:
            for char in word:
                letters.add(char)                
        smaller = {char:set() for char in letters}
        larger = {char:set() for char in letters}
        alienD = []
        seen = set()
        
        for i in range(1, len(words)):
            prev = words[i - 1]
            curr = words[i]
            j = 0
            while j < len(prev) and j < len(curr):
                if prev[j] != curr[j]:
                    smaller[curr[j]].add(prev[j])
                    larger[prev[j]].add(curr[j])
                    break
                j += 1
            if j == len(curr) and j < len(prev):
                return ''
        
        q = Queue()
        for l in letters:
            if len(smaller[l]) == 0:
                q.put(l)

        while not q.empty():
            can = q.get()
            alienD.append(can)
            seen.add(can)
            for ncan in larger[can]:
                smaller[ncan].remove(can)
                if len(smaller[ncan]) == 0:
                    if ncan in seen:
                        return ''
                    q.put(ncan)
                    
        if len(alienD) < len(letters):
            return ''
        
        return ''.join(alienD)
                
