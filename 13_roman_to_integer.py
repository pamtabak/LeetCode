class Solution:

    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        subtract = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
        result = 0
        i = 0
        last_char = ''
        while (i < len(s)):
            result += values[s[i]]
            if (last_char in subtract):
                if (s[i] in subtract[last_char]):
                    result -= 2 * values[last_char]
            last_char = s[i]
            i += 1
        return result
