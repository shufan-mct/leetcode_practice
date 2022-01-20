class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left < right:
            med = (left + right) // 2
            
            h_med  = 0
            for p in piles:
                h_med += p // med
                if p % med:
                    h_med += 1
            
            if h_med > h:
                left = med + 1
            else:
                right = med
                
        return left