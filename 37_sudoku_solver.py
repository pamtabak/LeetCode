from typing import List
from copy import deepcopy


class Solution:
    def isValidRowAndColumn(self, board: List[List[str]]) -> bool:
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
        return True

    def isValidSubboxes(self, board: List[List[str]]) -> bool:
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

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if (not self.isValidRowAndColumn(board)):
            return False

        return self.isValidSubboxes(board)

        return True

    def isSudokuComplete(self, board: List[List[str]]) -> bool:
        for row in range(0, len(board)):
            for column in range(0, len(board[row])):
                if (board[row][column] == "."):
                    return False
        return True

    def findRowColumn(self, board: List[List[str]]) -> bool:
        for row in range(0, len(board)):
            for column in range(0, len(board[row])):
                if (board[row][column] == "."):
                    return row, column
        return -1, -1

    def getColumn(self, board: List[List[str]], column: int) -> List[str]:
        columnList = []
        for row in range(0, len(board)):
            if (board[row][column] != "."):
                columnList.append(board[row][column])
        return columnList

    def findNumbersInSubbox(self, board: List[List[str]], row: int, column: int) -> List[str]:
        subbox = []
        firstRowIndex = 3*(row // 3)
        firstColumnIndex = 3*(column // 3)
        for r in range(firstRowIndex, firstRowIndex + 3):
            for c in range(firstColumnIndex, firstColumnIndex + 3):
                if (board[r][c] != "."):
                    subbox.append(board[r][c])
        return subbox

    def recursiveSudoku(self, board: List[List[str]]) -> None:
        if (self.isSudokuComplete(board)):
            return

        row, column = self.findRowColumn(board)
        columnList = self.getColumn(board, column)
        subbox = self.findNumbersInSubbox(board, row, column)

        for i in range(1, 10):
            if (str(i) in board[row] or str(i) in columnList or str(i) in subbox):
                continue
            if (self.isSudokuComplete(board) and self.isValidSudoku(board)):
                return
            board[row][column] = str(i)
            if (self.isValidSudoku(board)):
                self.recursiveSudoku(board)
            if (not self.isSudokuComplete(board)):
                board[row][column] = "."  # removing the operation we just made

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.recursiveSudoku(board)
