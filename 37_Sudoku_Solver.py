# -*- coding:utf-8 -*-

class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 用字典来存储每一行，每一列，每一个子box所填充过的数字
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    num=int(board[i][j])
                    rows[i][num]=rows[i].get(num, 0)+1
                    columns[j][num]=columns[j].get(num,0)+1
                    boxes[(i // 3) * 3 + j // 3][num]=boxes[(i // 3) * 3 + j // 3].get(num,0)+1

        def backtrack(row,col):
            #边界校验，如果填充到最后一个，表示结束返回true
            if col == len(board[0]):
                col=0
                row+=1
                if row==len(board):
                    return True

            if board[row][col]=='.':
                # 尝试填充1-9
                for num in range(1,10):
                    box_index = (row // 3) * 3 + col // 3
                    rows[row][num] = rows[row].get(num, 0)
                    columns[col][num] = columns[col].get(num, 0)
                    boxes[box_index][num] = boxes[box_index].get(num, 0)
                    can_use= not (rows[row][num]>=1 or  columns[col][num]>=1  or boxes[box_index][num]>=1)

                    if can_use:
                        rows[row][num]+=1
                        columns[col][num]+=1
                        boxes[box_index][num]+=1

                        board[row][col]=str(num)
                        if backtrack(row,col+1):
                            return True

                        board[row][col] = '.'
                        rows[row][num] -= 1
                        columns[col][num] -= 1
                        boxes[box_index][num] -= 1
            else:
                return backtrack(row,col+1)

        backtrack(0,0)

if __name__ == "__main__":
    board=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    r = Solution().solveSudoku(board)
    for i in range(len(board)):
        print board[i]
