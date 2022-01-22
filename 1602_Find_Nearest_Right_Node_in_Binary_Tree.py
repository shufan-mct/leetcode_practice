from queue import Queue

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = Queue()
        q.put(root)
        while not q.empty():
            levelLen = q.qsize()
            for i in range(levelLen):
                node = q.get()
                if node == u:
                    if i < levelLen - 1:
                        return q.get()
                    else:
                        return None
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        return None