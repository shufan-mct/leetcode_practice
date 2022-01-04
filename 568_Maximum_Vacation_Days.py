class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n = len(flights)
        k = len(days[0])

        outflows = [[city] for city in range(n)]
        for dep in range(n):
            for arr in range(n):
                if flights[dep][arr] == 1:
                    outflows[dep].append(arr)
        
        maxDays = [{} for week in range(k + 1)] # curr city: max total days so far 
        maxDays[0] = {0: 0}        
        
        for week in range(k):
            for city in maxDays[week]:
                for destination in outflows[city]:
                    if destination in maxDays[week + 1]:
                        maxDays[week + 1][destination] = max(maxDays[week + 1][destination], maxDays[week][city])
                    else:
                        maxDays[week + 1][destination] = maxDays[week][city]
            for city in maxDays[week + 1]:
                maxDays[week + 1][city] += days[city][week]
                
        maxTotal = 0
        for city in maxDays[week + 1]:
            maxTotal = max(maxTotal, maxDays[week + 1][city])
            
        return maxTotal
