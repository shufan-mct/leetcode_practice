class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]
        for i in range(len(nums)):
            if i == 0:
                left = 1
            else:
                left = nums[i - 1]
            if i == len(nums) - 1:
                right = 1
            else:
                right = nums[i + 1]
            dp[i][i] = left * nums[i] * right
        
        def burst(dp, i, j):
            if i > j :
                return 0            
            if dp[i][j] >= 0:
                return dp[i][j]
            if i == 0:
                left = 1
            else:
                left = nums[i - 1]
            if j == len(nums) - 1:
                right = 1
            else:
                right = nums[j + 1]
            maxCoins = -1
            for k in range(i, j + 1):
                coins = burst(dp, i, k - 1) + left * nums[k] * right + burst(dp, k + 1, j)
                maxCoins = max(maxCoins, coins)
            dp[i][j] = maxCoins
            return maxCoins
        
        return burst(dp, 0, len(nums) - 1)
        