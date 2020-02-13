# -*- coding:utf-8 -*-

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board :
            return

        row=len(board)
        col = len(board[0])
        # 从边界入手，如果边界为O，那么就看它临近的节点是否是O，若是O，都改为一个特殊字符，代表这些后面都不会变
        def helper(i,j):
            if i<0 or i>=row or j<0 or j>=col or board[i][j]=='X' or board[i][j]=='E':
                return

            board[i][j]='E'
            helper(i-1,j)
            helper(i + 1, j)
            helper(i, j-1)
            helper(i, j+1)
        # 上边界
        for j in range(col):
            if board[0][j]=='O':
                helper(0,j)
        # 下边界
        for j in range(col):
            if board[row-1][j]=='O':
                helper(row-1,j)
        # 左边界
        for i in range(row):
            if board[i][0]=='O':
                helper(i,0)
        # 右边界
        for i in range(row):
            if board[i][col-1]=='O':
                helper(i,col-1)

        for i in range(row):
            for j in range(col):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='E':
                    board[i][j]='O'


if __name__ == "__main__":
    board=[
        ['X','X','X','X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
    Solution().solve(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            print board[i][j]