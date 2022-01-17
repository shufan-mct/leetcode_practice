class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split()
        
        if len(sList) != len(pattern):
            return False
        
        n = len(sList)
        letToWord = {}
        encoded = set()
        
        for i in range(n):
            if pattern[i] not in letToWord:
                if sList[i] in encoded:
                    return False
                else:
                    letToWord[pattern[i]] = sList[i]
                    encoded.add(sList[i])
            elif letToWord[pattern[i]] != sList[i]:
                return False
        
        return True