class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        move_i = 0
        
        position = [0, 0]
        
        for char in instructions:
            if char == 'G':
                position[0] += move[(move_i) % 4][0]
                position[1] += move[(move_i) % 4][1]
            elif char == 'L':
                move_i -= 1
            else:
                move_i += 1
        
        return position == [0, 0] or (move_i) % 4 != 0