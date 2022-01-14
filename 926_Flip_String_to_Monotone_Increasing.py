class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        zeros = 0
        for i in range(n):
            if s[i] == '0':
                zeros += 1
        flip_0 = 0
        flip_1 = zeros
        
        minFlip = 0 + zeros
        for i in range(n):
            if s[i] == '0':
                flip_1 -= 1
                minFlip = min(minFlip, flip_1 + flip_0)
            else:
                flip_0 += 1
                    
        return minFlip