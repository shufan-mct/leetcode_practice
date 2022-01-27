public class Solution {
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
        int n = candies.Length;
        int maxCan = candies.Max();
        bool[] result = new bool[n];
        
        for (int i = 0; i < n; i ++){
            if (candies[i] + extraCandies >= maxCan){
                result[i] = true;
            }
            else{
                result[i] = false;
            }
        }
        
        return result;
    }
}