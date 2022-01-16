class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target == 1:
            return 0
        moves = 0
        
        while maxDoubles > 0:
            if target == 2:
                return moves + 1
            if target % 2 == 1:
                target -= 1
            else:
                maxDoubles -= 1
                target //= 2
            moves += 1
        
        return moves + (target - 1) 