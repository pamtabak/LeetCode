public class Solution {
    public int Reverse(int x) {
        try
        {
            string reverseX = String.Join("", x.ToString().Replace("-", "").Reverse().ToList());
            if (x < 0)
            {
                reverseX = "-" + reverseX;
            }
            return Int32.Parse(reverseX);
        }   
        catch (Exception ex)
        {
            return 0;
        }
    }
}