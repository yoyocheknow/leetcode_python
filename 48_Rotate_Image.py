# -*- coding:utf-8 -*-

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        if (row == 0 or col == 0):
            return None
        end = 0

        for i in range(1, row):
            end += 1
            for j in range(end):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        print matrix
        left = 0
        right = len(matrix[0]) - 1

        while (left < right):
            for row in range(len(matrix)):
                temp = matrix[row][left]
                matrix[row][left] = matrix[row][right]
                matrix[row][right] = temp

            left += 1
            right -= 1
        return matrix
if __name__ == "__main__":
    matrix=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
    r = Solution().rotate(matrix)
    print r