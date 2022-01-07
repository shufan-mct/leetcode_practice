class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        Sum = 0
        digit = n
        while digit > 0:
            remainder = digit % 10
            product *= remainder
            Sum += remainder
            digit = digit // 10
        return product - Sum