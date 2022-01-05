class Solution:
    def encode(self, num: int) -> str:
        if num == 0:
            return ''
        
        digits = 1
        lower = 1
        upper = 2
        levelLen = 2
        while upper < num:
            lower = upper + 1
            levelLen *= 2
            upper += levelLen
            digits += 1
        
        code = ['0'] * digits
        reduced = num - lower
        i = digits - 1
        while reduced > 0:
            if reduced % 2:
                code[i] = '1'
            i -= 1
            reduced = reduced // 2
        
        return ''.join(code)