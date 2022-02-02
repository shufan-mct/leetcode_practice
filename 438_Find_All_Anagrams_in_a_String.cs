public class Solution {
    public IList<int> FindAnagrams(string s, string p) {
        int sLen = s.Length;
        int pLen = p.Length;
        IList<int> idx = new List<int>();
        
        if (pLen > sLen){
            return idx;
        }
        
        int[] sCount = new int[26];
        int[] pCount = new int[26];
        
        
        for (int i = 0; i < pLen; i ++){
            sCount[Encode(s[i])] += 1; 
        }
        for (int i = 0; i < pLen; i ++){
            pCount[Encode(p[i])] += 1;
        }
        
        if (ElementCompare(sCount, pCount)){
            idx.Add(0);
        }
        
        for (int i = 1; i <= sLen - pLen ; i ++){
            sCount[Encode(s[i - 1])] -= 1;
            sCount[Encode(s[i + pLen - 1])] += 1;
            if (ElementCompare(sCount, pCount)){
                idx.Add(i);
            }
        }
        
        return idx;
        
    }
    
    private bool ElementCompare(int[] letterCount1, int[] letterCount2){
        for (int i = 0; i < 26; i ++){
            if (letterCount1[i] != letterCount2[i]){
                return false;
            }
        }
        return true;
    }
    
    private int Encode(char c){
        return (int)c - (int)'a';
    }
}