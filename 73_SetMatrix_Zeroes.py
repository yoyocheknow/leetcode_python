# -*- coding:utf-8 -*-


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        zero_index=[]
        # zero_index存储 为0 的行号和列号
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    zero_index.append([i,j])
        print zero_index
        # 把行号为0 的行置为0，把列号为0 的所在列置为0
        for k in range(len(zero_index)):
            zero_row=zero_index[k][0]
            for j in range(col):
                matrix[zero_row][j]=0

            zero_col = zero_index[k][1]
            for i in range(row):
                matrix[i][zero_col] = 0

        return


if __name__ == "__main__":
    matrix=[[0,1]]
    r = Solution().setZeroes(matrix)
    print matrix