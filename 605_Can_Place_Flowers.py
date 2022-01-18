class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plants = 0
        lastPlanted = -2
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i - 1 >= 0 and flowerbed[i - 1] == 1:
                continue
            if i + 1 < len(flowerbed) and flowerbed[i + 1] == 1:
                continue
            if i - lastPlanted < 2:
                continue
                
            plants += 1
            lastPlanted = i
            
        return plants >= n