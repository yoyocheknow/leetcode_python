# -*- coding:utf-8 -*-

class Solution(object):
    # 此方法用到了递归，会超时
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

    def isMatch2(self, s, p):
        s_length = len(s)
        p_length = len(p)
        # dp[i][j]表示s[0...i],p[0...j]匹配
        dp = [[-1 for col in range(p_length + 1)] for row in range(s_length + 1)]

        # Empty s and Empty p
        dp[0][0]=1
        #下面是标记情况
        # empty p
        for i in range(1,len(dp)):
            dp[i][0]=0
        # empty s
        for i in range(1,len(dp[0])):
            if p[i-1]=='*':
                dp[0][i]=dp[0][i-1]
            else:
                dp[0][i]=0
        #状态转移方程
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    #p[j-1]='*'的话，可以作为任意字符匹配，也可以作为空匹配
                    dp[i][j]=dp[i][j-1]|dp[i-1][j]|dp[i-1][j-1]
                elif s[i-1]!=p[j-1]:
                    dp[i][j]=0
        return dp[s_length][p_length]==1
if __name__ == "__main__":
    r = Solution().isMatch2('aa','*')
    print r
