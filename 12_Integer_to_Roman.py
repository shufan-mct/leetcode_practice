class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, 'M'), (900,'CM'), (500, 'D'), (400, 'CD'),
                  (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                  (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
                  (1,'I')]
        roman = []
        for val, let in digits:
            num, count = num % val, num // val
            roman.append(let * count)
        return ''.join(roman)