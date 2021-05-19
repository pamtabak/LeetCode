class Solution:
    def intToRoman(self, num: int) -> str:
        values = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
                  40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        keys = sorted(values)
        index = len(keys) - 1
        result = ""
        while (num > 0):
            if (num < keys[index]):
                index -= 1
                continue
            result += values[keys[index]]
            num -= keys[index]
        return result
