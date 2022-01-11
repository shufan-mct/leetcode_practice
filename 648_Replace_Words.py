class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = TrieNode()
        for word in dictionary:
            node = trie
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = True
            
        senList = sentence.split()
        for i in range(len(senList)):
            word = senList[i]
            node = trie
            i_replace = 0
            for char in word:
                if char not in node.children:
                    i_replace = None
                    break
                node = node.children[char]
                i_replace += 1
                if node.word:
                    break
            if i_replace is not None:
                senList[i] = senList[i][:i_replace]
        
        return ' '.join(senList)