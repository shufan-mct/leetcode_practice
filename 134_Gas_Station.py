class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gain = []
        for i in range(n):
            gain.append(gas[i] - cost[i])
        
        prevSum = 0
        
        end = n - 1
        curr = 0
        while curr <= end:
            prevSum += gain[curr]
            while prevSum < 0:
                prevSum += gain[end]
                end -= 1
                if end < curr:
                    return -1
            curr += 1
            
        return (end + 1) % n