class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for count, char in (a, 'a'), (b, 'b'), (c, 'c'):
            if count > 0:
                heapq.heappush(max_heap, (-count, char))
        lgst = []
        while max_heap:
            count1, can1 = heapq.heappop(max_heap)  
            if len(lgst) >= 2 and lgst[-1] == lgst[-2] == can1:
                if max_heap:
                    count2, can2 = heapq.heappop(max_heap)
                    lgst.append(can2)
                    count2 += 1
                    if count2 < 0:
                        heapq.heappush(max_heap, (count2, can2))
                    heapq.heappush(max_heap, (count1, can1))
                else:
                    break
            else:
                lgst.append(can1)
                count1 += 1
                if count1 < 0:
                    heapq.heappush(max_heap, (count1, can1))
        return ''.join(lgst)