class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalin(string):
            i = 0
            j = len(string) - 1
            while i < j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def backtracking(s, path, start, valid):
            if start == len(s):
                valid.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if isPalin(s[start:end]):
                    path.append(s[start:end])
                    backtracking(s, path, end, valid)
                    path.pop()
        
        valid = []
        backtracking(s, [], 0, valid)
        return valid