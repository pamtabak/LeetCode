class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_number = ""
        for digit in digits:
            str_number += str(digit)
        number = int(str_number)
        number += 1
        result = []
        str_number = str(number)
        for c in str_number:
            result.append(int(c))
        return result
