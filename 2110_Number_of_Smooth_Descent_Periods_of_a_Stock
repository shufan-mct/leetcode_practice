class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 0
        local = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                local += 1
            else:
                count += (local + 1) * local // 2
                local = 1
        count += (local + 1) * local // 2
        return count