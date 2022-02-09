public class Solution {
    public int DeleteAndEarn(int[] nums) {
        int[] count = new int[10001];
        foreach (int num in nums) count[num]++;
        
        int earn_prev2 = 0;
        int earn_prev1 = 0;
        int curr = 0;
        
        for (int i = 1; i < 10001; i ++){
            curr = Math.Max(earn_prev2 + i * count[i], earn_prev1);
            earn_prev2 = earn_prev1;
            earn_prev1 = curr;
        }
        
        return curr;        
    }
}