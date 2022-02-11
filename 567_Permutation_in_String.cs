public class Solution {
    public bool CheckInclusion(string s1, string s2) {
        if (s1.Length > s2.Length) return false;
        
        int[] letterCount1 = new int[26];
        int[] letterCount2 = new int[26];
        int meetCount = 0;
        
        foreach (char c in s1) letterCount1[(int)c - (int)'a'] += 1;
        for (int i = 0; i < s1.Length; i++ ) letterCount2[(int)s2[i] - (int)'a'] += 1;
        for (int i = 0; i < 26; i++ ){
            if (letterCount1[i] == letterCount2[i]) meetCount += 1;
        }
        if (meetCount == 26){return true;}
        
        for (int i = 0; i < s2.Length - s1.Length; i++ ){
            int charStart = (int) s2[i] - (int)'a';
            int charEnd = (int) s2[i + s1.Length] - (int)'a';
            
            if (letterCount1[charStart] == letterCount2[charStart]) meetCount -= 1;
            letterCount2[charStart] -= 1;
            if (letterCount1[charStart] == letterCount2[charStart]) meetCount += 1;
            
            if (letterCount1[charEnd] == letterCount2[charEnd]) meetCount -= 1;
            letterCount2[charEnd] += 1;
            if (letterCount1[charEnd] == letterCount2[charEnd]) meetCount += 1;
            
            if (meetCount == 26) return true;
        }
        
        return false;
    }
}