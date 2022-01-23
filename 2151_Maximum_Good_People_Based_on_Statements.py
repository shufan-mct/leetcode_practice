class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        guess = [0]* n
        maxGood = 0
        
        def check(statements, guess, n, i, good):
            if i == 0:
                return True
            if good:
                for prev in range(i):
                    if guess[prev] == 1:
                        if statements[prev][i] == 0 or statements[i][prev] == 0:
                            return False
                    else:
                        if statements[i][prev] == 1:
                            return False
            elif not good:
                for prev in range(i):
                    if guess[prev] == 1:
                        if statements[prev][i] == 1:
                            return False
                        
            return True
        
        def backtracking(statements, guess, n, i):
            nonlocal maxGood
            if i == n:
                maxGood = max(maxGood, sum(guess))
                return
                            
            if check(statements, guess, n, i, 1):
                guess[i] = 1
                backtracking(statements, guess, n, i + 1)
            if check(statements, guess, n, i, 0):
                guess[i] = 0
                backtracking(statements, guess, n, i + 1)
        
        backtracking(statements, guess, n, 0)
        return maxGood
        