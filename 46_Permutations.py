class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permute = []
        
        def backtracking(nums, i, permute):
            if i == len(nums):
                permute.append(nums[:])
                return
            backtracking(nums, i + 1, permute)
            for j in range(i + 1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtracking(nums, i + 1, permute)
                nums[i], nums[j] = nums[j], nums[i]
            
        backtracking(nums, 0, permute)
        return permute