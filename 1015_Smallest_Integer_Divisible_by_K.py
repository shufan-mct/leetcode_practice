class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rems = set()
        rem = 1 % k
        l = 1
        while rem not in rems:
            if rem == 0:
                return l
            rems.add(rem)
            rem = (rem * 10 + 1) % k
            l += 1
        return -1