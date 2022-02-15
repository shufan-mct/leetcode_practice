public class Solution {
    public int SingleNumber(int[] nums) {
        HashSet<int> once = new HashSet<int>();
        
        foreach(int num in nums){
            if(once.Contains(num)) once.Remove(num);
            else once.Add(num);
        }
        
        foreach(int n in once) return n;
        
        return 0;
    }
}