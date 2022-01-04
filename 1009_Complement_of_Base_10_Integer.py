class Solution:
    def bitwiseComplement(self, n: int) -> int:
        twoSum = 1
        while twoSum < n:
            twoSum = twoSum * 2 + 1
        return twoSum - n