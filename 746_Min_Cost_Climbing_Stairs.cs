public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        int n = cost.Length;
        int[] minCost = new int[n];
        minCost[n - 1] = cost[n - 1];
        minCost[n - 2] = cost[n - 2];
        
        for (int i = n - 3; i >= 0; i --){
            minCost[i] = cost[i] + Math.Min(minCost[i + 1], minCost[i + 2]);
        }
        
        return Math.Min(minCost[0], minCost[1]);
    }
}