class Solution:
    def minDeletions(self, s: str) -> int:
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
        maxCount = max(counts)
        freqs = collections.Counter(counts)
        stack = []
        dels = 0
        for count in range(maxCount, -1, -1):
            if freqs[count] > 1:
                for j in range(freqs[count] - 1):
                    stack.append(count)
            elif freqs[count] == 0:
                if stack:
                    dels += stack.pop() - count
        while stack:
            dels += stack.pop()
        return dels