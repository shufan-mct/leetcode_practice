class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        
        count = [0] * 101 # num: count
        for num in arr:
            count[num] += 1
        
        # x <= y <= z
        ans = 0
        
        # x != y, y != z
        for x in range(target // 3 + 1):
            for y in range(x + 1, (target - x)//2 + 1):
                z = target - x - y
                if y < z <= 100:
                    ans += count[x] * count[y] * count[z]
                    ans %= MOD
        
        # x == y, y!= z
        for x in range(target // 3 + 1):
            z = target - x - x
            if x < z <= 100:
                ans += count[x] * (count[x] - 1) * count[z]// 2
                ans %= MOD
                
        # x != y, y == z
        for x in range(target // 3 + 1):
            if (target - x) % 2 == 0:
                y = (target - x) // 2
                if x < y <= 100:
                    ans += count[x] * count[y] * (count[y] - 1) // 2
                    ans %= MOD
                    
        # x== y == z
        if target % 3 == 0:
            x = target // 3
            ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
            ans %= MOD
        
        return ans