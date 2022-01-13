class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda point : point[1])
        last_end = -float('inf')
        arrows = 0
        
        for start, end in points:
            if start > last_end:
                arrows += 1
                last_end = end
            
        return arrows