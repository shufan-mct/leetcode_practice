class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        increase = {} # time: increment
        
        for start, end in intervals:
            increase[start] = increase.get(start, 0) + 1
            increase[end] = increase.get(end, 0) - 1
            
        rooms = 0
        maxRooms = 0
        for time in sorted(increase):
            rooms += increase[time]
            maxRooms = max(rooms, maxRooms)
            
        return maxRooms