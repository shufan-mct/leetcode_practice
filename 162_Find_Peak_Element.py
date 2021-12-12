class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            med = (left + right) // 2
            if nums[med] > nums[med + 1]:
                right = med
            else:
                left = med + 1
        return left
