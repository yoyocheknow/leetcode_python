# -*- coding:utf-8 -*-

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g_l=len(g)
        s_l=len(s)
        g.sort()
        s.sort()
        i,j=0,0
        while(i<g_l and j<s_l):
            if g[i]<=s[j]:
                # 糖果序列j满足孩子序列i，两个指针都向后移动
                i+=1
                j+=1
            elif g[i]>s[j]:
                # 糖果序列j不满足孩子序列i，则糖果指针向后移动，尝试找到更大的糖果
                j+=1

        return i

if __name__ == "__main__":
    r = Solution().findContentChildren([1,2,3], [1,2,3])
    print r
