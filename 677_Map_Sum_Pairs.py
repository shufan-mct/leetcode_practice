class TrieNode:
    def __init__(self):
        self.val = 0
        self.children = {}

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {} # key : value

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.val += diff

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.val