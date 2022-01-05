# Both BFS and DFS solutions included. 
# Their classes are named differently to disguish. 

from queue import Queue

class CodecBFS:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = []
        q = Queue()
        q.put(root)
        while not q.empty():
            layerLen = q.qsize()
            for i in range(layerLen):
                node = q.get()
                if node:
                    string.append(str(node.val))
                    q.put(node.left)
                    q.put(node.right)
                else:
                    string.append('N')
        return '.'.join(string)
                        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'N':
            return None
        string = data.split('.')
        root = TreeNode(int(string[0]))        
        q = Queue()
        q.put(root)
        for i in range(1, len(string)):            
            if string[i] == 'N':
                child = None
            else:
                child = TreeNode(int(string[i]))
                q.put(child)
            if i % 2:
                par = q.get()
                par.left = child
            else:
                par.right = child
        return root

class CodecDFS:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = []
        self.preOrder(string, root)
        return '.'.join(string)
        
    def preOrder(self, string, root):
        if not root:
            string.append('N')
            return
        string.append(str(root.val))
        self.preOrder(string, root.left)
        self.preOrder(string, root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        string = data.split('.')
        return self.buildTree(string, 0)[0]
        
    def buildTree(self, string, start):
        if string[start] == 'N':
            return (None, start)
        root = TreeNode(int(string[start]))
        root.left, leftEnd = self.buildTree(string, start + 1)
        root.right, rightEnd = self.buildTree(string, leftEnd + 1)
        return (root, rightEnd)