# Link: https://leetcode.com/problems/range-sum-query-2d-immutable/description/

"""Problem Description:
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.
"""

# Solution: T.C: O(); S.C: O()
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ=0
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                summ+=self.matrix[row][col]
        return summ
