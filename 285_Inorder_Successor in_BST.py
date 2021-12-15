class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        curr = root
        succ = None
        while curr:
            if curr.val <= p.val:
                curr = curr.right
            else:
                succ = curr
                curr = curr.left
        return succ