class Solution:
    def convert(self, s: str, numRows: int) -> str:
        grids = [[] for r in range(numRows)]
        down = numRows
        up = max(numRows - 2, 0)
        for i, char in enumerate(s):
            remainder = i % (up + down)
            if 0 <= remainder < down:
                grids[remainder].append(char)
            else:
                grids[up + down - remainder].append(char)
        for r in range(len(grids)):
            grids[r] = ''.join(grids[r])
        return ''.join(grids)