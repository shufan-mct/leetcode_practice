class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        last = self.countAndSay(n - 1)
        count = 1
        value = last[0]
        result = []
        for i in range(1, len(last)):
            if last[i] == value:
                count += 1
            else:
                result.append(str(count))
                result.append(value)
                value = last[i]
                count = 1
        result.append(str(count))
        result.append(value)
        return ''.join(result)
