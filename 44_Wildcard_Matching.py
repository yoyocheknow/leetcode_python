# -*- coding:utf-8 -*-

class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_length = len(s)
        p_length= len(p)
        # dp[i][j]表示s[0...i],p[0...j]匹配
        dp=[[-1 for col in range(p_length+1)] for row in range(s_length+1)]
        dp[s_length][p_length]=1
        for col in range(p_length-1,-1,-1):
            dp[s_length][col] = dp[s_length][col+1] if p[col]=='*' else 0

        for row in range(s_length):
            dp[row][p_length]=0
        self.dfsHelper(dp,s,p,0,0)
        print dp
        return dp[0][0]==1

    def dfsHelper(self,dp,s,p,sp,pp):

        if(dp[sp][pp]!=-1):
            return dp[sp][pp]

        if(s[sp]==p[pp] or p[pp]=='?'):
            dp[sp][pp] = self.dfsHelper(dp,s, p, sp + 1, pp + 1)
        elif(p[pp]=='*'):
            # p中的*可以替换前面的所有序列
            resultOne = self.dfsHelper(dp,s, p, sp + 1, pp)
            # p中的*作为空
            resultTwo = self.dfsHelper(dp,s, p, sp, pp + 1)
            # p中的* 作为对应的字符
            resultThree = self.dfsHelper(dp,s, p, sp + 1, pp + 1)

            dp[sp][pp] = 1 if (resultOne + resultTwo + resultThree) > 0 else 0
        else:
            dp[sp][pp]=0

        return dp[sp][pp]
if __name__ == "__main__":
    r = Solution().isMatch('abceb','*a*b')
    print r
