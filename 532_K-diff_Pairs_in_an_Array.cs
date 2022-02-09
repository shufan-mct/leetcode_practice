public class Solution {
    public int FindPairs(int[] nums, int k) {
        HashSet<int> seen = new HashSet<int>();
        int pairs = 0;
        
        if (k == 0){
            HashSet<int> found = new HashSet<int>();
            
            foreach (int num in nums){
                if (found.Contains(num)) continue;
                if (seen.Contains(num)){
                    pairs += 1;
                    found.Add(num);
                }
                else seen.Add(num);
            }
            
            return pairs;
        }

        foreach (int num in nums){
            if (seen.Contains(num)) continue;
            if (seen.Contains(num + k)) pairs += 1;
            if (seen.Contains(num - k)) pairs += 1;
            seen.Add(num);
        }
                
        return pairs;        
    }
}