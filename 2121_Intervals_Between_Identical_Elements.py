class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        numIdx = {}
        numPointer = {}
        for i, n in enumerate(arr):
            if n in numIdx:
                numIdx[n].append(numIdx[n][-1] + i)
            else:
                numIdx[n] = [i]
                numPointer[n] = 0
        intervals = []
        for i, n in enumerate(arr):
            pointer = numPointer[n]
            prefixSum = numIdx[n]
            interval = i * (2 * pointer  + 2 - len(numIdx[n]) )
            interval -= prefixSum[pointer]
            interval += prefixSum[-1] - prefixSum[pointer]
            numPointer[n] += 1
            intervals.append(interval)            
        return intervals