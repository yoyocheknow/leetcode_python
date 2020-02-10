# -*- coding:utf-8 -*-

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 这个题抽象一下就是给出的数子中，有的可以是一个数的组合，有的是两个数的组合（两个数的组合必须是小于等于26）
        # 这样的话，那就和爬楼梯的思路基本一样了，n阶楼梯可以一次一个台阶也可以1次两个台阶。
        # 用dp的思路来做这道题，dp[i]代表到达第i个数字时，一共有几种组合方式
        # 如果s[i-1]>=1的话，dp[i]=dp[i-1],因为上一个数字是>=1的，那么第i个数字，就可以已独立的形式，即一个数字作为一个组合出现
        # 如果前两个数字可以作为一个组合的话，那么dp[i]=dp[i-1]+dp[i-2],
        # 如果前一个数字是0 的话，那么肯定是和前面第二个数字组合在一起的。所以是dp[i]=dp[i-2]（dp[i]初始化为0）
        size=len(s)
        dp=[0]*(size+1)
        dp[0]=1
        for i in range(1,size+1):
            value=int(s[i-1])
            if value>=1:
                dp[i]=dp[i-1]
            if i>1:
                v=int(s[i-2])
                add = v*10+value
                if add>=10 and add<=26:
                    dp[i]+=dp[i-2]

        return dp[size]

if __name__ == "__main__":

    r = Solution().numDecodings('1228')
    print r