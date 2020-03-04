# -*- coding:utf-8 -*-

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 这个思路是借助栈。每当s[i]=='('时，就apppend进去，当s[i]==')'则pop掉最后一个元素
        # 这个时候判断栈是否为空，若为空，则把当前i放入栈中，代表此时已经遍历出一个全新的匹配，与后面的匹配长度无关
        # 记录下当前index的原因是，计算后面匹配的括号的长度
        # 若不为空则计算出当前i和栈顶的差值即为一个合法匹配的长度。
        stack=[-1]
        res=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res=max(res,i-stack[-1])
        return res

    def longestValidParentheses2(self, s):
        # 这个思路是从左到右，和从右到左分别扫描s
        # 从左到右扫描，记录'('，')'长度，若两者相等，则记录此时匹配的长度。若')'长度大于'('长度，则重新计算
        # 从右到左扫描逻辑和上面类似
        left,right,res=0,0,0
        for i in range(len(s)):
            if s[i]=='(':
                left+=1
            else:
                right+=1
            if left==right:
                res=max(res,left+right)
            elif right>left:
                left=0
                right=0

        left,right=0,0
        for i in range(len(s)-1,0,-1):
            if s[i]=='(':
                left+=1
            else:
                right+=1
            if left==right:
                res=max(res,left+right)
            elif left>right:
                left=0
                right=0

        return res
if __name__ == "__main__":
    r = Solution().longestValidParentheses2('(()')

    print r
