class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        camera = 0
        
        # 0 : leaf
        # 1 : parent of a leave, camera
        # 2 : covered
        def findPosition(root):
            nonlocal camera
            if not root:
                return 2
            l = findPosition(root.left)
            r = findPosition(root.right)
            if l == 0 or r == 0:
                camera += 1
                return 1
            if l == 1 or r == 1:
                return 2
            return 0
        
        return (findPosition(root) == 0) + camera