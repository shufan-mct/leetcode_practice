class Solution {
    public int CountShips(Sea sea, int[] topRight, int[] bottomLeft) {
        if (!sea.HasShips(topRight, bottomLeft)) return 0;
        
        int left = bottomLeft[0];
        int right = topRight[0];
        int top = topRight[1];
        int bottom = bottomLeft[1];
        
        if (left == right & top == bottom) return 1;
        
        int midHori = (left + right) / 2;
        int midVert = (top + bottom) / 2; 
        
        int areaLoLe = CountShips(sea, new int[] {midHori, midVert}, bottomLeft);
        int areaLoRi = CountShips(sea, new int[] {right, midVert}, new int[] {midHori + 1, bottom});
        int areaUpLe = CountShips(sea, new int[] {midHori, top}, new int[] {left, midVert + 1});
        int areaUpRi = CountShips(sea, topRight, new int[] {midHori + 1, midVert + 1});
        
        return areaLoLe + areaLoRi + areaUpLe + areaUpRi;
    }
}