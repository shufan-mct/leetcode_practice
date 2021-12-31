class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = []
        
        def height(root, leaves):
            if not root:
                return -1
            h = max(height(root.left, leaves), height(root.right, leaves)) + 1
            if len(leaves) == h:
                leaves.append([])
            leaves[h].append(root.val)
            return h
        
        height(root, leaves)
        return leaves