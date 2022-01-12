class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = TrieNode()
        for product in products:
            node = trie
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = True
        
            
        def DFS(root, preStr, i, result):
            if len(result[i]) >= 3:
                return
            for char in sorted(root.children):
                if len(result[i]) >= 3:
                    return
                node = root.children[char]
                string = preStr + char
                if node.word:
                    result[i].append(string)
                DFS(node, string, i, result)
        
        result = [[] for i in range(len(searchWord))]
        root = trie
        for i in range(len(searchWord)):
            char = searchWord[i]
            if char not in root.children:
                return result
            root = root.children[char]
            if root.word:
                result[i].append(searchWord[:i + 1])
            DFS(root, searchWord[:i + 1], i, result)
        
        return result