class Solution:
    def creatingNewMatrix (self, matrix: List[List[int]]) -> List[List[int]]:
        #first solution: not solving it in place. did this just to better understand the solution. This seems to work
        newMatrix: List[List[int]] = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix)):
                row.append(0)
            newMatrix.append(row)
        
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(matrix)):
                newMatrix[j][len(matrix) - 1 - i] = row[j]
        
        return newMatrix
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #each row i becomes column len(matrix) - i
        #to do it in place, we need to rotate each "external" square
        matrixSize = len(matrix)
        for i in range(0, math.ceil(matrixSize/2)):
            for j in range(0, matrixSize//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[matrixSize - j - 1][i]
                matrix[matrixSize - j - 1][i] = matrix[matrixSize - i - 1][matrixSize - j - 1]
                matrix[matrixSize - i - 1][matrixSize - j - 1] = matrix[j][matrixSize - i - 1]
                matrix[j][matrixSize - i - 1] = tmp
                
                
