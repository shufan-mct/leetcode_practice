class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        split1 = count[0]
        split2 = count[0] + count[1]
        for i in range(len(nums)):
            if i < split1:
                nums[i] = 0
            elif i < split2:
                nums[i] = 1
            else:
                nums[i] = 2
        return
