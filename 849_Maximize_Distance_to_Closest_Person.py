class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxDis = 0
        prevTaken = None
        for i, num in enumerate(seats):
            if num == 1:
                if prevTaken is None:
                    maxDis = i
                else:
                    maxDis = max(maxDis, (i - prevTaken) // 2)
                prevTaken = i
                    
        maxDis = max(maxDis, (len(seats)- 1 - prevTaken))
        return maxDis