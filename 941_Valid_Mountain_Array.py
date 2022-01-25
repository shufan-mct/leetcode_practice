class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        while i < len(arr) - 1 and arr[i] < arr[i + 1]:
            i += 1
            
        if i == 0 or i == len(arr) - 1:
            return False
        
        while i < len(arr) - 1:
            if arr[i] <= arr[i + 1]:
                return False
            i += 1
            
        return True