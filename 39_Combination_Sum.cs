public class Solution {
    public IList<IList<int>> CombinationSum(int[] candidates, int target) {
        IList<IList<int>> combs = new List<IList<int>>();
        Backtrack(0, 0, new List<int>(), target, candidates, combs);
        return combs;
    }
    
    protected void Backtrack(
        int startIdx, int prevSum, IList<int> prevPath, 
        int target, int[] candidates, IList<IList<int>> combs){
        
        if (prevSum == target){
            IList<int> path = new List<int>(prevPath);
            combs.Add(path);
            return;
        }
        
        if (prevSum > target) return;
        
        for (int i = startIdx; i < candidates.Length; i++){
            //prevSum += candidates[i];
            prevPath.Add(candidates[i]);
            Backtrack(i, prevSum + candidates[i], prevPath, target, candidates, combs);
            prevPath.RemoveAt(prevPath.Count - 1);
        }
        return;
        
    }
}