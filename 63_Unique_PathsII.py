# -*- coding:utf-8 -*-

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row= len(obstacleGrid)
        col=len(obstacleGrid[0])

        if obstacleGrid[0][0]==1:
            return 0
        obstacleGrid[0][0]=1

        for i in range(1,row):
            # 先处理第一列，这条路径只能从上往下走，只要有一个位置为0 ，那么下面的均为0，无法到达
            obstacleGrid[i][0]=int(obstacleGrid[i][0]==0 and obstacleGrid[i-1][0]==1)

        for j in range(1,col):
            # 处理第一行，这条路径只能从左往右走，只要有一个位置为0 ，那么后面的均为0，无法到达
            obstacleGrid[0][j]=int(obstacleGrid[0][j]==0 and obstacleGrid[0][j-1]==1)

        for i in range(1,row):
            for j in range(1,col):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j]=0
        return obstacleGrid[-1][-1]
if __name__ == "__main__":
    obstacleGrid=[
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    r = Solution().uniquePathsWithObstacles(obstacleGrid)
    print r
