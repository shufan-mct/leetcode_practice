class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        maxSum = 0
        minSum = 0
        for start in range(len(nums)):
            max_ = nums[start]
            min_ = nums[start]
            for end in range(start, len(nums)):
                max_ = max(max_, nums[end])
                min_ = min(min_, nums[end])
                maxSum += max_
                minSum += min_
        return maxSum - minSum
