class Solution:
    def countPoints(self, rings: str) -> int:
        colors = [[0,0,0] for i in range(10)]
        mapping = {'R':0, 'G':1, 'B':2}
        for i in range(len(rings)//2):
            color = mapping[rings[2 * i]]
            rod = int(rings[2 * i + 1])
            colors[rod][color] = 1
        count = 0
        for c in colors:
            if sum(c) == 3:
                count += 1
        return count
