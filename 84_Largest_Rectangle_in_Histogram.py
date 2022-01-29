class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def expandFromMid(heights, left, right):
            mid = (left + right) //2
            height = heights[mid]
            crossArea = heights[mid]
            p1 = mid - 1
            p2 = mid + 1
            
            while p1 >= left or p2 < right:
                if p2 == right:
                    height = min(height, heights[p1])
                    p1 -= 1
                elif p1 < left:
                    height = min(height, heights[p2])
                    p2 += 1
                elif heights[p1] > heights[p2]:
                    height = min(height, heights[p1])
                    p1 -= 1
                else:
                    height = min(height, heights[p2])
                    p2 += 1
                currArea = height * (p2 - p1 - 1)
                crossArea = max(crossArea, currArea)
            return crossArea
                    
        
        def maxArea(heights, left, right):
            if left == right:
                return 0
            
            crossArea = expandFromMid(heights, left, right)
            leftArea = maxArea(heights, left, (left + right) //2)
            rightArea = maxArea(heights, (left + right) //2 + 1, right)
            return max(crossArea, leftArea, rightArea)
        
        return maxArea(heights, 0, len(heights))