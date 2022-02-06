public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int count = 1;
        int idxWrite = 1;
        for (int i = 1; i < nums.Length; i ++){
            if (nums[i] != nums[i - 1]){
                count = 1;
            }
            else {
                count += 1;
            }
            
            if (count <= 2){
                nums[idxWrite] = nums[i];
                idxWrite += 1;
            }
            
        }
        
        return idxWrite;
    }
}