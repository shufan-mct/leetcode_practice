class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        if ord('A') <= ord(word[0]) <= ord('Z'):
            cap_1 = ord('A') <= ord(word[1]) <= ord('Z')
            for i in range(2, len(word)):
                cap_i = ord('A') <= ord(word[i]) <= ord('Z')
                if cap_i != cap_1:
                    return False
        
        else:
            for i in range(1, len(word)):
                if ord('A') <= ord(word[i]) <= ord('Z'):
                    return False
        
        return True