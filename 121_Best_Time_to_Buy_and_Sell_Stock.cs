public class Solution {
    public int MaxProfit(int[] prices) {
        int minPrice = prices[0];
        int maxProfit = 0;
        foreach (int price in prices){
            maxProfit = Math.Max(maxProfit, price - minPrice);
            minPrice = Math.Min(minPrice, price);
        }
        return maxProfit;
    }
}