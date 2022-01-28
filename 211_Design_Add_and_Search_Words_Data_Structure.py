class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        
        def search_i(word, i, node):
            if i == len(word):
                return node.end
            if word[i] == '.':
                if not node.children:
                    return False
                for charCan in node.children:
                    if search_i(word, i + 1, node.children[charCan]):
                        return True
                return False
            else:
                if word[i] in node.children:
                    return search_i(word, i + 1, node.children[word[i]])
                else:
                    return False
                    
        return search_i(word, 0, self.root)