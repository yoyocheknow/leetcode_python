# -*- coding:utf-8 -*-


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        if board == [[]]:
            return False

        used = {}
        self.i = 0
        def check(i, j):

            if board[i][j] != word[self.i]:
                return False

            # make sure we have not used before
            key = (i, j)
            if key in used:
                return False
            used[key] = 1
            self.i+=1
            # if length matches we are done!
            if self.i == len(word):
                return True
            # try going down
            if i + 1 < row and check(i + 1, j):
                return True
            # try going right
            if j + 1 < col and check(i, j + 1):
                return True
            # try going up
            if i - 1 >= 0 and check(i-1, j):
                return True
            # try going left
            if j- 1 >= 0 and check(i, j-1):
                return True
            self.i -= 1
            del used[key]  # step back

            return False


        for i in range(row):
            for j in range(col):
                if check(i, j):
                    return True

        return False

if __name__ == "__main__":
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    r = Solution().exist(board,"ABCB")
    print r