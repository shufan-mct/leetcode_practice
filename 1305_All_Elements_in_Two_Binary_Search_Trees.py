# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        trav1, trav2 = [], []
        
        def inOrder(root, trav):
            if not root:
                return
            inOrder(root.left, trav)
            trav.append(root.val)
            inOrder(root.right, trav)
        
        inOrder(root1, trav1)
        inOrder(root2, trav2)
        
        allElems = []
        p1 = 0
        p2 = 0
        
        while p1 < len(trav1) or p2 < len(trav2):
            if p1 == len(trav1):
                allElems.append(trav2[p2])
                p2 += 1
                continue
            if p2 == len(trav2):
                allElems.append(trav1[p1])
                p1 += 1
                continue
            if trav1[p1] <= trav2[p2]:
                allElems.append(trav1[p1])
                p1 += 1
            else:
                allElems.append(trav2[p2])
                p2 += 1
        
        return allElems
            