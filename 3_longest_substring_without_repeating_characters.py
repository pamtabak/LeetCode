class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = ""
        for i in range(0, len(s)):
            # assuming substring will start in s[i]
            seen_letters = {}
            current_substring = ""
            for j in range(i, len(s)):
                if (s[j] in seen_letters):
                    break
                seen_letters[s[j]] = True
                current_substring += s[j]
            if (len(current_substring) > len(longest_substring)):
                longest_substring = current_substring
        print(longest_substring)
        return len(longest_substring)
