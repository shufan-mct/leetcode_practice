class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        maxSplit = 1
        
        def backtracking(s, i, split):
            nonlocal maxSplit
            if i == len(s) - 1:
                split[i] = 1
                maxSplit = max(maxSplit, uniqSplit(s, split))
                return
            split[i] = 1
            backtracking(s, i + 1, split)
            split[i] = 0
            backtracking(s, i + 1, split)
            
        def uniqSplit(s, split):
            substr = set()
            start = 0
            for i, sp in enumerate(split):
                if sp == 0:
                    continue
                end = i + 1
                if s[start: end] in substr:
                    return  -1
                substr.add(s[start: end])
                start = end
            return len(substr)
        
        backtracking(s, 0, [0]*len(s))
        return maxSplit
            
                
            