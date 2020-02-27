# -*- coding:utf-8 -*-

class Solution(object):
    # dp[i]表示金额i所需要的最少张数
    # 状态转移方程：dp[i]= min(dp[i-coins[j]])+1
    # 即dp[14]=min(dp[1],dp[2],dp[5],dp[7],dp[10])+1

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[-1]*(amount+1)
        dp[0]=0

        for i in range(1,amount+1):
            for j in range(len(coins)):
                # dp[i-coins[j]]!=-1 代表i-coin[j] 有这样差额的硬币，比如14-7=7 ，dp[7]=1有7块这样的硬币
                if i-coins[j]>=0 and dp[i-coins[j]]!=-1:
                    if dp[i]==-1 or dp[i]>dp[i-coins[j]]+1:
                        dp[i]=dp[i-coins[j]]+1
        return dp[amount]

    def coinChange2(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":

    r = Solution().coinChange([1,2,5,7,10],14)
    print r
