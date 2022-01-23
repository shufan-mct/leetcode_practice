class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        lonely = []
        
        for num in counter:
            if counter[num] == 1 and counter[num - 1] == 0 and counter[num + 1] == 0:
                lonely.append(num)
                
        return lonely