class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        chunks = 0
        start = 0
        i = 0
        
        while start < n:
            end = start
            while i <= end:
                if arr[i] > end:
                    end = arr[i]
                i += 1
            chunks += 1
            start = i
        
        return chunks