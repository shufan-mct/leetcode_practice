class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        curr = x
        rnum = 0
        while curr > 0:
            rnum = rnum * 10 + curr % 10
            curr = curr // 10
        return rnum == x