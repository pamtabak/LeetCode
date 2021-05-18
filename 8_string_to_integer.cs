public class Solution {
    public int MyAtoi(string s) {
        s = s.TrimStart();
        if (String.IsNullOrEmpty(s) || (!Char.IsDigit(s[0]) && s[0] != '+' && s[0] != '-' ))
        {
            return 0;
        }
        
        bool negativeNumber = s[0] == '-';
        if (s[0] == '+' || s[0] == '-')
        {
            s = s.Substring(1);
        }
        string resultString = "";
        foreach (char c in s)
        {
            if (!Char.IsDigit(c))
            {
                break;
            }
            resultString += c;
        }
        if (String.IsNullOrEmpty(resultString))
        {
            return 0;
        }
        if (negativeNumber)
        {
            resultString = "-" + resultString;
        }
        
        try
        {
            return Int32.Parse(resultString);
        }
        catch
        {
            if (negativeNumber)
            {
                return -2147483648;
            }
            else
            {
                return Int32.Parse((Math.Pow(2, 31) - 1).ToString());
            }
        }
    }
}