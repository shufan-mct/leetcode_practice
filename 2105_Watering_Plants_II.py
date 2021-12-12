class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        refill = 0
        a = capacityA
        b = capacityB
        left = 0
        right = len(plants) - 1
        while left < right:
            if a < plants[left]:
                a = capacityA
                refill += 1
            if b < plants[right]:
                b = capacityB
                refill += 1
            a -= plants[left]
            b -= plants[right]
            left += 1
            right -= 1
        if left != right:
            return refill
        if max(a,b) >= plants[left]:
            return refill
        else:
            return refill + 1
