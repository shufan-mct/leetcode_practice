class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        increase = {} # position: number of increased passengers
        
        for num, from_, to in trips:
            increase[from_] = increase.get(from_, 0) + num
            increase[to] = increase.get(to, 0) - num
        
        carFill = 0
        for pos in sorted(increase):
            carFill += increase[pos]
            if carFill >  capacity:
                return False
        
        return True