public class Solution {
    public char FindTheDifference(string s, string t) {
        int[] sCount = new int[26];
        int[] tCount = new int[26];
        
        foreach (char c in s){
            sCount[(int)c - (int)'a'] += 1;
        }
        
        foreach (char c in t){
            tCount[(int)c - (int)'a'] += 1;
        }
        
        for (int i = 0; i < 26; i ++){
            if (tCount[i] > sCount[i]){
                return (char) (i + (int)'a');
            }
        }
        
        return '-';
    }
}