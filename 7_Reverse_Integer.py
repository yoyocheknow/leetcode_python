# -*- coding:utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x<0 else 1

        x = abs(x)
        temp_list=[]
        while(x/10>0):
            temp = x%10
            temp_list.append(temp)
            x= (x-temp) /10
        temp_list.append(x)
        length = len(temp_list)
        res=0
        for i in temp_list:
            res=res+i* (10 **(length-1))
            length-=1

        if res * sign > 2 ** 31 - 1 or res * sign < -1 * (2 ** 31):
            return 0
        return res * sign

if __name__ == "__main__":
    r = Solution().reverse(1534236469)
    print r
