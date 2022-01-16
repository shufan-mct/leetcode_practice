class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        divided = []
        
        for i in range(len(s) // k):
            divided.append(s[i * k : (i + 1)* k])
        
        if len(s) % k != 0:
            last = s[- (len(s)% k):] + fill * (k - len(s)% k)
            divided.append(last)
            
        return divided