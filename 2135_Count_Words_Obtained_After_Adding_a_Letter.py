class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startSet = set()
        for sw in startWords:
            swl = list(sw)
            swl.sort()
            startSet.add(''.join(swl))
        
        count = 0

        for tw in targetWords:
            twl = list(tw)
            twl.sort()
            for i in range(len(twl)):
                char = twl[i]
                twl[i] = ''
                if (''.join(twl)) in startSet:
                    count += 1
                    break
                twl[i] = char
        
        return count