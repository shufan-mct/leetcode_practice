public class Solution {  
    public void Rotate(int[] nums, int k) {
        int n = nums.Length;
        k %= n;
        Queue<int> savedNums = new Queue<int>();
        for (int i = n - k; i < n; i++){
            savedNums.Enqueue(nums[i]);
        }
        for (int i = 0; i < n; i++){
            savedNums.Enqueue(nums[i]);
            nums[i] = savedNums.Dequeue();
        }
    }
}
