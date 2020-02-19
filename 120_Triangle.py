# -*- coding:utf-8 -*-

class Solution(object):
    # dp思想 dp[i][j]表示从下到上，最小的路径值
    # 那么初始化dp[row-1][0...col-1]=triangle[row-1][0...col-1]
    # dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
    # 最后dp[0][0]是目标所求的值，返回即可
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        col = len(triangle[-1])

        dp=[[0 for i in range(col)] for j in range(row)]

        for i in range(col):
            dp[row-1][i]=triangle[row-1][i]

        for i in range(len(triangle)-2,-1,-1):

            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]

        return dp[0][0]


if __name__ == "__main__":
    taiangle=[
     [2],
     [3,4],
     [6,5,7],
     [4,1,8,3]
    ]
    r = Solution().minimumTotal(taiangle)
    print r
