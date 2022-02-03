class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        sum12count = {}
        count = 0
        
        for i in range(n):
            for j in range(n):
                sum12 = nums1[i] + nums2[j]
                sum12count[sum12] = sum12count.get(sum12, 0) + 1
        
        for i in range(n):
            for j in range(n):
                sum34 = nums3[i] + nums4[j]
                count += sum12count.get(-sum34, 0)
                
        return count