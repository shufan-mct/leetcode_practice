class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def encode(string):
            slist = ['a']
            for i in range(1, len(string)):
                diff = (ord(string[i]) - ord(string[0])) % 26
                slist.append(chr(ord('a') + diff))
            return ''.join(slist)
        
        encoded = {}
        for s in strings:
            en_s = encode(s)
            if en_s not in encoded:
                encoded[en_s] = []
            encoded[en_s].append(s)
        
        groups = []
        for en_s in encoded:
            groups.append(encoded[en_s])
        
        return groups