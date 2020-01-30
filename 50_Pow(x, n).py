# -*- coding:utf-8 -*-

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def power(x, n):
            if n == 0:
                return 1
            half = power(x, n//2)
            if n % 2 == 0:
                return half*half
            else:
                return half*half *x
        if n < 0:
            return 1/power(x, -n)
        else:
            return power(x, n)

if __name__ == "__main__":
    r = Solution().myPow(2.00000, 3)
    print r