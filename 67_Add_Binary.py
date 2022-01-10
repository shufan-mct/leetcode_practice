class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i1 = len(a) - 1
        i2 = len(b) - 1
        Sum = []
        carry = 0
        
        while i1 >= 0 or i2 >= 0:
            d1 = int(a[i1]) if i1 >= 0 else 0
            d2 = int(b[i2]) if i2 >= 0 else 0
            dsum = d1 + d2 + carry
            Sum.append(str(dsum % 2))
            carry = dsum // 2
            i1 -= 1
            i2 -= 1
            
        if carry == 1:
            Sum.append(str(carry))
        
        Sum.reverse()
        return ''.join(Sum)