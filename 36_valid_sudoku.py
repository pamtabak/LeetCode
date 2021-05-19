class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows and columns
        for row in range(0, len(board)):
            rowSeenNumbers = {}
            columnSeenNumbers = {}
            for column in range(0, len(board[row])):
                rowItem = board[row][column]
                columnItem = board[column][row]
                if (rowItem != "." and rowItem in rowSeenNumbers):
                    return False
                if (columnItem != "." and columnItem in columnSeenNumbers):
                    return False
                rowSeenNumbers[rowItem] = True
                columnSeenNumbers[columnItem] = True
        # validate each subbox
        for i in range(0, 3):
            for j in range(0, 3):
                boxSeenNumbers = {}
                for row in range(i*3, i*3 + 3):
                    for column in range(j*3, j*3 + 3):
                        rowItem = board[row][column]
                        if (rowItem != "." and rowItem in boxSeenNumbers):
                            return False
                        boxSeenNumbers[rowItem] = True
        return True
