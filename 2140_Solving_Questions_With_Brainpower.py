class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        maxEarn = [0] * n
        maxEarn[n - 1] = questions[n - 1][0]
        
        i = n - 2
        while i >= 0:
            maxEarn[i] = maxEarn[i + 1]
            earn = questions[i][0]
            if i + questions[i][1] + 1 < n:
                earn += maxEarn[i + questions[i][1] + 1]
            maxEarn[i] = max(earn, maxEarn[i])
            i -= 1
        
        return maxEarn[0]