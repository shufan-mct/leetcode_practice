public class Solution {
    public int Rob(int[] nums) {
        int n = nums.Length;
        
        if (n == 1){
            return nums[0];
        }
        
        List<int> robbed = new List<int>();
        robbed.Add(nums[0]);
        robbed.Add(Math.Max(nums[0], nums[1]));
        
        for (int i = 2; i < n; i ++){
            robbed.Add(Math.Max(robbed[i - 2] + nums[i], robbed[i - 1]));
        }
        
        return Math.Max(robbed[n - 2], robbed[n - 1]);
        
    }
}