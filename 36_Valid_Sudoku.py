# -*- coding:utf-8 -*-

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        col_list=[[],[],[],[],[],[],[],[],[]]
        child_9=[[],[],[],[],[],[],[],[],[]]
        for i in range(len(board)):
            row_list=[]
            for j in range(len(board[i])):

                if board[i][j]!='.':
                    if board[i][j] not in row_list:
                        #检查每一行是否有效
                        row_list.append(board[i][j])
                    else:
                        return False
                    if board[i][j] not in col_list[j]:
                        #检查每一列是否有效
                        col_list[j].append(board[i][j])
                    else:
                        return False
                    # child_9[i]是每一个子数独
                    if i<=2:
                        if j<=2:
                            child_9[0].append(board[i][j])
                        elif j<=5:
                            child_9[1].append(board[i][j])
                        else:
                            child_9[2].append(board[i][j])
                    elif i<=5:
                        if j<=2:
                            child_9[3].append(board[i][j])
                        elif j<=5:
                            child_9[4].append(board[i][j])
                        else:

                            child_9[5].append(board[i][j])
                    else:
                        if j<=2:

                            child_9[6].append(board[i][j])
                        elif j<=5:
                            child_9[7].append(board[i][j])
                        else:
                            child_9[8].append(board[i][j])

        for i in range(len(child_9)):
            temp=[]
            for j in range(len(child_9[i])):

                if child_9[i][j] not in temp:
                    temp.append(child_9[i][j])
                else:
                    return False

        return True

    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True





if __name__ == "__main__":
    board=[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    r = Solution().isValidSudoku(board)
    print r