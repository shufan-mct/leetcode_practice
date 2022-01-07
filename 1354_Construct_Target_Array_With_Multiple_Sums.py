class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        
        
        totalSum = sum(target)
        heap = [-num for num in target]
        heapq.heapify(heap)
        
        while -heap[0] > 1:
            prevSum = - heapq.heappop(heap)
            restSum = totalSum - prevSum
            if restSum == 1:
                return True
            prevNum = prevSum % restSum
            if prevNum == 0 or prevNum == prevSum:
                return False
            heapq.heappush(heap, -prevNum)
            totalSum = totalSum - prevSum + prevNum
            
        return True