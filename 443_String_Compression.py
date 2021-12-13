class Solution:
    def compress(self, chars) -> int:
        prev = chars[0]
        count = 0
        index = 0
        
        def adjustStr(chars, index, prev, count):
            chars[index] = prev
            index += 1
            if count > 1:
                sCount = str(count)
                for i in range(len(sCount)):
                    chars[index] = sCount[i]
                    index += 1                
            return index
        
        for char in chars:
            if char == prev:
                count += 1
            else:
                index = adjustStr(chars, index, prev, count)
                prev = char
                count = 1
        
        return adjustStr(chars, index, prev, count)
