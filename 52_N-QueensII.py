# -*- coding:utf-8 -*-


class Solution(object):

    def is_valid(self,queen_positions,i,j):
        for x,y in queen_positions:
            if x==i or y==j or x+y==i+j or x-y==i-j:
                return False
        return True

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[]

        def backtrack(queens,queen_positions,row):
            if row==n:
                res.append(queens)
                return
            for j in range(n):
                if self.is_valid(queen_positions,row,j):
                    queens[i] = "." * j + "Q" + "." * (n - j - 1)

                    backtrack(queens,queen_positions+[(row,j)],row+1)

                    queens[i] = "." * n
        queens=['.'* n for i in range(n)]
        backtrack(queens,[],0)
        return len(res)

if __name__ == "__main__":

    r = Solution().totalNQueens(4)

    print r