public class Solution {
    public int MaximumWealth(int[][] accounts) {
        int customers = accounts.Length;
        int maxWealth = 0;
        for (int i = 0; i < customers; i++){
            maxWealth = Math.Max(maxWealth, accounts[i].Sum());
        }
        return maxWealth;
    }
}