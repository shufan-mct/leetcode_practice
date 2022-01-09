class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        
        if total == 0 or total == n:
            return 0
    
        minSwap = n
        inRange = 0
        for i in range(total):
            inRange += nums[i]
        minSwap = min(minSwap, total - inRange)
        
        for start in range(n):
            end = (start + total) % n            
            inRange -= nums[start]
            inRange += nums[end]
            minSwap = min(minSwap, total - inRange)

        return minSwap