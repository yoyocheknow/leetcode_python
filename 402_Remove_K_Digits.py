# -*- coding:utf-8 -*-


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res=[]
        for i in range(len(num)):
            number=int(num[i])
            while(len(res)!=0 and number<res[-1] and k>0):
                res.pop(-1)
                k-=1

            if number!=0 or len(res)!=0:

                res.append(number)

        while (len(res)!=0 and k>0):
            res.pop()
            k-=1
        if len(res)==0:
            return '0'
        else:
            return ''.join(str(i) for i in res)

if __name__ == "__main__":
    r = Solution().removeKdigits("10200", 1)
    print r

