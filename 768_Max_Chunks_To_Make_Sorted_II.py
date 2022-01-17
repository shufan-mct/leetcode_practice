class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        
        maxFromLeft = [arr[0]] * n
        for i in range(1, n):
            maxFromLeft[i] = max(maxFromLeft[i - 1], arr[i])
        
        minFromRight = [arr[-1]] * n
        for i in range(n - 2, -1, -1):
            minFromRight[i] = min(minFromRight[i + 1], arr[i])
            
        chunks = 0
        for i in range(n - 1):
            if maxFromLeft[i] <= minFromRight[i + 1]:
                chunks += 1
        
        chunks += 1
        
        return chunks