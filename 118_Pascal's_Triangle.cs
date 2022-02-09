public class Solution {
    public IList<IList<int>> Generate(int numRows) {
        IList<IList<int>> triangle = new List<IList<int>>();
        triangle.Add(new List<int>(){1});
                
        for (int i = 1; i < numRows; i ++){
            triangle.Add(new List<int>());
            triangle[i].Add(1);
            
            for (int j = 1; j < i; j ++){
                triangle[i].Add(triangle[i - 1][j - 1] + triangle[i - 1][j]);
            }
            
            triangle[i].Add(1);                        
        }
        
        return triangle;
    }
}