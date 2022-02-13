public class Solution {
    
    IList<IList<int>> subsets = new List<IList<int>>();
    
    public IList<IList<int>> Subsets(int[] nums) {
        Backtracking(0, new List<int>(), nums);
        return subsets;        
    }
    
    public void Backtracking(int i, List<int> path, int[] nums){
        if (i == nums.Length) {            
            subsets.Add(new List<int>(path));
            return;
        }
        
        path.Add(nums[i]);
        Backtracking(i + 1, path, nums);
        path.RemoveAt(path.Count - 1);
        Backtracking(i + 1, path, nums);
    }        
        
}