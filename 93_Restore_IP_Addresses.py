class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        
        def isValid(s):
            if len(s) == 1:
                return True
            if 1 < len(s) <= 3:
                if s[0] == '0':
                    return False
                elif 0 < int(s) < 256:
                    return True
            return False
            
        def addToList(s, end1, end2, end3, restored):
            add = []
            add.append(s[:end1])
            add.append(s[end1: end2])
            add.append(s[end2: end3])
            add.append(s[end3:])
            restored.append('.'.join(add))
            
        def split(s, restored):
            for end1 in range(1, 4):
                if not isValid(s[:end1]):
                    continue
                for end2 in range(end1 + 1, end1 + 4):
                    if not isValid(s[end1: end2]):
                        continue
                    for end3 in range(end2 + 1, end2 + 4):
                        if not isValid(s[end2: end3]) or not isValid(s[end3:]):
                            continue
                        addToList(s, end1, end2, end3, restored)
        
        restored = []
        split(s, restored)
        return restored