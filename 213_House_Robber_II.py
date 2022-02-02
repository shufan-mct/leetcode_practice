class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        skip_first = [0, nums[1]]
        for i in range(2, n):
            skip_first.append(max(skip_first[i - 2] + nums[i], skip_first[i - 1]))
        
        skip_last = [nums[0], max(nums[0], nums[1])]
        for i in range(2, n - 1):
            skip_last.append(max(skip_last[i - 2] + nums[i], skip_last[i - 1]))        
        
        return max(skip_first[-1], skip_first[-2], skip_last[-1], skip_last[-2])