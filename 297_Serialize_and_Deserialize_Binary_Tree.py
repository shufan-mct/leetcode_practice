from queue import Queue

class Codec:
    
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
        par = root
        for i in range(1, len(string) - 1):
            if string[i] == 'N':
                child = None
            else:
                child = TreeNode(int(string[i]))
                q.put(child)
            if i % 2:
                par.left = child
            else:
                par.right = child
                par = q.get()
        return root
