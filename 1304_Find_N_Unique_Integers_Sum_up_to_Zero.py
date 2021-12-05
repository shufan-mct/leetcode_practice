class Solution:
    def sumZero(self, n: int) -> List[int]:
        nums = []
        for i in range(1, n // 2 + 1):
            nums.append(-i)
            nums.append(i)
        if n % 2 == 1:
            nums.append(0)
        return nums
