class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        strL = ['']
        while a > 0 or b > 0:
            if len(strL) > 2 and strL[-1] == strL[-2]:
                writeA  = strL[-1] == 'b'
            else:
                writeA = a >= b
                
            if writeA:
                strL.append('a')
                a -= 1
            else:
                strL.append('b')
                b -= 1
        return ''.join(strL)