class Leaderboard:

    def __init__(self):
        self.board = {} # {id : score}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.board:
            self.board[playerId] += score
        else:
            self.board[playerId] = score

    def top(self, K: int) -> int:
        heap = []
        for player in self.board:
            heapq.heappush(heap, self.board[player])
            if len(heap) > K:
                heapq.heappop(heap)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.board.pop(playerId)
