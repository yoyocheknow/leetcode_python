# -*- coding:utf-8 -*-

class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        result = ''
        if n==1:
            return '1'
        else:
            s=self.countAndSay(n-1)
            p=1
            while(s):
                if s=='1':
                    result += '11'
                    s = s[1:]
                elif s[p:p+1]==s[p-1:p]:
                    p+=1
                    continue
                else:
                    result=result+str(p)+s[p-1:p]
                    s=s[p:]
                    p=1
            return result


if __name__ == "__main__":
    r = Solution().countAndSay(6)
    print r