class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def insertion(root, val):
            if val > root.val:
                if root.right:
                    insertion(root.right, val)
                else:
                    root.right = TreeNode(val)
            else:
                if root.left:
                    insertion(root.left, val)
                else:
                    root.left = TreeNode(val)
                    
        insertion(root, val)
        return root