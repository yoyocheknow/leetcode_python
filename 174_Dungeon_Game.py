# -*- coding:utf-8 -*-


class Solution(object):
    # dp[i][j]表示要到达i,j，最少需要的血量。所以要从右下往左上递推，最后返回dp[0][0]即可。
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 1
        row = len(dungeon)
        col = len(dungeon[0])

        dp =[[0 for j in range(col)] for i in range(row)]
        # 到达右下角时，若[row-1][col-1]为正，则是补血，那么此时骑士最少血量应为1
        # 若[row-1][col-1]为负，则是扣血，那么此时骑士血量最少应为1-dungeon[row-1][col-1]
        dp[row-1][col-1] = max(1, 1-dungeon[row-1][col-1])

        for i in range(row-2,-1,-1):
            dp[i][col-1] = max(1, dp[i+1][col-1] - dungeon[i][col-1] )

        for j in range(col-2,-1,-1):
            dp[row-1][j] = max(1, dp[row-1][j+1] - dungeon[row-1][j])

        for i in range(row-2,-1,-1):
            for j in range(col-2,-1,-1):
                # 因为要求最小，而且可能向下走或者向右走，所以找到最小的下一个
                dp_min= min(dp[i+1][j],dp[i][j+1])
                dp[i][j] = max(1, dp_min - dungeon[i][j])

        return dp[0][0]

if __name__ == "__main__":
    dungeon=[
     [-2,-3,3],
     [-5,-10,1],
     [10,30,-5]
    ]
    r = Solution().calculateMinimumHP(dungeon)
    print r