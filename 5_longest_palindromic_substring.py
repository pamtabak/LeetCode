class Solution:
    def isPalindrome(self, s):
        reverse_s = s[::-1]
        return s == reverse_s

    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        for i in range(0, len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                current_substring = s[i:j+1]
                if (len(current_substring) < len(longest_palindrome)):
                    break
                if (self.isPalindrome(current_substring)):
                    if (len(current_substring) > len(longest_palindrome)):
                        longest_palindrome = current_substring
        return longest_palindrome
