class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        def helper(n, dp):
            if dp[n] != -1:
                return dp[n]
            root = int(math.sqrt(n))
            for r in range(1, root + 1):
                remove = r * r
                if helper(n - remove, dp) == 0:
                    dp[n] = 1
                    return 1
            dp[n] = 0
            return 0
        
        return helper(n, dp)