class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDif = 0
        
        def pathDiff(root, prevMax, prevMin):
            if not root:
                return
            nonlocal maxDif
            maxDif = max(maxDif, abs(prevMax - root.val), abs(prevMin - root.val))
            prevMax = max(prevMax, root.val)
            prevMin = min(prevMin, root.val)
            pathDiff(root.left, prevMax, prevMin)
            pathDiff(root.right, prevMax, prevMin)
            
        pathDiff(root, root.val, root.val)
        
        return maxDif