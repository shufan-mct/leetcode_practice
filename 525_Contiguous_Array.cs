public class Solution {
    public int FindMaxLength(int[] nums) {
        int n = nums.Length;
        Dictionary<int, int> diffIdx = new Dictionary<int, int>();
        diffIdx.Add(0, -1);
        int diff = 0; // diff = zeros - ones
        int maxLen = 0;
        
        for (int i = 0; i < n; i ++){
            diff += - 2 * nums[i] + 1;
            if (diffIdx.ContainsKey(diff)){
                maxLen = Math.Max(maxLen, i - diffIdx[diff]);
            }
            else{
                diffIdx[diff] = i;
            }
        }
        
        return maxLen;
    }
}