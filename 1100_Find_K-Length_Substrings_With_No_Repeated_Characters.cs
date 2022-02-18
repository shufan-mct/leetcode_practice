public class Solution {
    public int NumKLenSubstrNoRepeats(string s, int k) {
        if (k > 26) return 0;
        
        int[] freq = new int[26];
        int substrK = 0;
        int left = 0, right = 0;
        
        while (right < s.Length){
            freq[s[right] - 'a'] += 1;
            while (freq[s[right] - 'a'] > 1){
                freq[s[left] - 'a'] -= 1;
                left += 1;
            }
            
            if (right - left + 1 == k){
                substrK += 1;
                freq[s[left] - 'a'] -= 1;
                left += 1;
            }
            
            right += 1;
        }
        
        return substrK;
    }
}