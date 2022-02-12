from queue import Queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordToWord = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                wordToWord[key].append(word)
        
        q = Queue()
        q.put(beginWord)
        seen = set()
        level = 1
        while not q.empty():
            levelLen = q.qsize()
            for i in range(levelLen):
                currWord = q.get()
                if currWord in seen:
                    continue
                if currWord == endWord:
                    return level
                for i in range(len(currWord)):
                    keyWord = currWord[:i] + '*' + currWord[i + 1:]
                    for nextWord in wordToWord[keyWord]:
                        q.put(nextWord)
                seen.add(currWord)
            level += 1
                
        return 0