# -*- coding:utf-8 -*-
import copy

class Solution(object):



    def solveNQueens2(self, n):
        # i代表行，j代表列。下一个（i，j)是否有效，要看已经落子的皇后的位置
        # 不能落在同一行，同一列，还有以落子皇后为中心的y=x方向，和y=-x方向上
        # i==x 表示同一行，j==y表示同一列，i-j==x-y表示 y=x方向，i+j==x+y 表示y=-x方向

        def isvalid(i, j, queen_positions):
            for x, y in queen_positions:
                if i==x or j == y or i - j == x - y or i + j == x + y:
                    return False
            return True

        def dfs(temp, i, queen_positions, res):
            if i == n:
                res.append(temp[:])
            for j in range(n):
                if isvalid(i, j, queen_positions):
                    temp[i] = "." * j + "Q" + "." * (n - j - 1)
                    dfs(temp, i + 1, queen_positions + [(i, j)], res)
                    temp[i] = "." * n

        temp = ["." * n for i in range(n)]
        res = []
        dfs(temp, 0, [], res)
        return res




    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 此思路是维护了一个mark二维数组，初始化为0，每加入一个皇后，不能落子的位置置为1，
        # 然后从第一行开始循环，每落一子，就更新mark位置，然后递归地去落下一行，找到mark[i,j]不为0的地方落子
        # 如果到了最后一行，说明这个方案可行，加入结果集。如果遍历完每一行，都不行，那么就回退，再从上一行的下一列开始继续回溯。
        # 期间要保留mark数组，回退完以后要复原上一次的状态
        mark=[[0 for i in range(n)] for j in range(n)]
        location=[['.' for i in range(n)] for j in range(n)]
        result=[]
        def backtrack(k,n,mark,location):
            if k==n:
                temp_location = copy.deepcopy(location)
                result.append(temp_location)
                return
            for i in range(n):
                if mark[k][i]==0:
                    temp_mark=copy.deepcopy(mark)
                    location[k][i]='Q'
                    self.put_down_queen(k,i,mark)
                    backtrack(k+1,n,mark,location)
                    mark=temp_mark
                    location[k][i]='.'
        backtrack(0,n,mark,location)
        return result

    def put_down_queen(self,x,y,mark):
        dx=[0,-1,-1,-1,0,1,1,1]
        dy=[-1,-1,0,1,1,1,0,-1]
        mark[x][y]=1
        for i in range(1,len(mark)):
            for j in range(8):
                new_x=x+i*dx[j]
                new_y=y+i*dy[j]
                if new_x>=0 and new_x<len(mark) and new_y>=0 and new_y<len(mark):
                    mark[new_x][new_y]=1
        return mark


if __name__ == "__main__":

    r = Solution().solveNQueens2(4)

    print r
