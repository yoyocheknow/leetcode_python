# -*- coding:utf-8 -*-


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start=1
        while(x/start>=start):
            start+=1

        return start-1

if __name__ == "__main__":
    r = Solution().mySqrt(100)
    print r