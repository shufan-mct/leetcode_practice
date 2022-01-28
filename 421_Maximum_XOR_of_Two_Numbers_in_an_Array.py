class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None
        self.val = 0
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        binNums = ["{0:b}".format(num).zfill(32) for num in nums]
        root = TrieNode()
        
        for i, binNum in enumerate(binNums):
            curr = root
            for digit in binNum:
                if digit == '0':
                    if curr.zero is None:
                        curr.zero = TrieNode()
                    curr = curr.zero
                else:
                    if curr.one is None:
                        curr.one = TrieNode()
                    curr = curr.one
            curr.val = nums[i]
                    
        maxXOR = 0
        for i, binNum in enumerate(binNums):
            curr = root
            for digit in binNum:
                if digit == '0':
                    if curr.one:
                        curr = curr.one
                    else:
                        curr = curr.zero
                else:
                    if curr.zero:
                        curr = curr.zero
                    else:
                        curr = curr.one
            maxXOR = max(maxXOR, curr.val ^ nums[i])
            
        return maxXOR