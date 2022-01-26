public class Solution {
    public int[] RunningSum(int[] nums) {
        int n = nums.Length;
        int[] rSums = new int[n];
            
        rSums[0] = nums[0];
        
        for (int i = 1; i < nums.Length; i++){
            rSums[i] = rSums[i - 1] + nums[i];
        }
        
        return rSums;
    }
}