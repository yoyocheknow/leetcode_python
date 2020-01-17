# -*- coding:utf-8 -*-

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        int_max = 2**31-1
        int_min = -1*(2**31-1)
        if dividend==0:
            return 0
        sign_dividend = 1 if dividend>0 else -1
        sign_divisor = 1 if divisor >0 else -1
        dividend = abs(dividend)
        divisor=abs(divisor)
        toggle = 1 if sign_dividend == sign_divisor else -1

        q, times = 0, 0
        while dividend >= divisor:
            temp = dividend - (divisor << times)
            if temp >= 0:
                q += (1 << times)
                times += 1
                dividend = temp
            else:
                times -= 1
        result = q * toggle
        if result >int_max:
            return int_max
        else:
            return result

if __name__ == "__main__":
    r = Solution().divide(-2147483648,1)
    print r
