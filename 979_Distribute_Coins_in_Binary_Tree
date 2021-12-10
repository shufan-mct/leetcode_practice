class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        def coinsRequired(node):
            nonlocal moves
            if not node:
                return 0
            leftReq = coinsRequired(node.left)
            rightReq = coinsRequired(node.right)
            req = 1 - node.val + leftReq + rightReq
            moves += abs(leftReq) + abs(rightReq)
            return req
        coinsRequired(root)
        return moves
