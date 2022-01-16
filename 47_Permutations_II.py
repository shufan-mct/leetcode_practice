class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permute = []
        
        def backtracking(nums, i, permute):
            if i == len(nums):
                permute.append(nums[:])
                return
            
            backtracking(nums, i + 1, permute)
            
            appeared = set()
            appeared.add(nums[i])
            for j in range(i + 1, len(nums)):
                if nums[j] in appeared:
                    continue
                    
                nums[i], nums[j] = nums[j], nums[i]
                backtracking(nums, i + 1, permute)
                nums[i], nums[j] = nums[j], nums[i]
                appeared.add(nums[j])
            
        backtracking(nums, 0, permute)
        return permute