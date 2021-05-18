class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = []
        for i in range(0, numRows):
            matrix.append([])
        row = 0
        increase = True
        for letter in s:
            if (row == (numRows - 1)):
                increase = False
            elif (row == 0):
                increase = True
            matrix[row].append(letter)
            if (increase and numRows > 1):
                row += 1
            elif (not increase and numRows > 1):
                row -= 1
        result = ""
        for row in matrix:
            for column in row:
                result += column
        return result
