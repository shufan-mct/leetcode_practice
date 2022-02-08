public class Solution {
    public int AddDigits(int num) {
        if (num < 10){
            return num;
        }
        
        int digSum = 0;
        while (num > 0){
            digSum += num % 10;
            num = num / 10;
        }
        
        return AddDigits(digSum);
    }
}