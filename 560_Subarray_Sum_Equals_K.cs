public class Solution {
    public int SubarraySum(int[] nums, int k) {
        int prefixSum = 0;
        Dictionary<int, int> sumCount = new Dictionary<int, int>(){{0, 1}};
        int subCount = 0;
        
        foreach (int num in nums){
            prefixSum += num;
            if (sumCount.ContainsKey(prefixSum - k)) subCount += sumCount[prefixSum - k];
            if (sumCount.ContainsKey(prefixSum)) sumCount[prefixSum] += 1;
            else sumCount.Add(prefixSum, 1);
        }
        
        return subCount;
        
    }
}