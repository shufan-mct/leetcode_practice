class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        def rotate(box):
            col = len(box)
            row = len(box[0])
            rotated = [ [box[col - c - 1][r] for c in range(col)]for r in range(row)]
            return rotated
        
        def fall(rotated):
            row = len(rotated)
            col = len(rotated[0])
            for c in range(col):
                stone = 0
                for r in range(row):
                    if rotated[r][c] == '#':
                        stone += 1
                        rotated[r][c] = '.'
                    elif rotated[r][c] == '*':
                        fillRow = r - 1
                        while stone > 0:
                            rotated[fillRow][c] = '#'
                            stone -= 1
                            fillRow -= 1
                fillRow = row - 1
                while stone > 0:
                    rotated[fillRow][c] = '#'
                    stone -= 1
                    fillRow -= 1
            return rotated
        
        rotated = rotate(box)
        return fall(rotated)