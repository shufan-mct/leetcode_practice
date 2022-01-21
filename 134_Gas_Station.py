class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        prevGain = 0
        minGain = float('inf')
        minGainIdx = 0
        
        for i in range(n):
            prevGain += gas[i] - cost[i]
            if prevGain < minGain:
                minGain = prevGain
                minGainIdx  = i
                
        if prevGain < 0:
            return -1
        else:
            return (minGainIdx + 1) % n