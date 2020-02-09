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

        self.used = {}
        self.i = 0

        def check(i, y):
            if board[y][x] != word[self.i]:
                return False

            # make sure we have not used before
            key = (x, y)
            if key in self.used:
                return False
            self.used[key] = 1
            self.i += 1

            # if length matches we are done!
            if self.i == len(word):
                return True
            # try going right
            if x + 1 < len(board[0]) and check(x + 1, y):
                return True
            # try going down
            if y + 1 < len(board) and check(x, y + 1):
                return True
                # try going up
            if y - 1 >= 0 and check(x, y - 1):
                return True
            # try going left
            if x - 1 >= 0 and check(x - 1, y):
                return True
            self.i -= 1
            del self.used[key]  # step back

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