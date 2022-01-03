class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        
        trustVotes = [0] * (n + 1)
        
        for person, trusted in trust:
            trustVotes[person] -= 1
            trustVotes[trusted] += 1
            
        for can in range(1, n + 1):
            if trustVotes[can] == n - 1:
                return can
            
        return -1