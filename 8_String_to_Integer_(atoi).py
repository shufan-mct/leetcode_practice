class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        findInt = False
        num = 0
        i = 0
        
        while i < len(s) and s[i] == ' ':
            i += 1
            
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                negative = True
            i += 1
            
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        if negative:
            num = - num 
        num = min(num, 2 ** 31 - 1)
        num = max(num, - 2 ** 31)
        
        return num