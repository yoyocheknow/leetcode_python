# -*- coding:utf-8 -*-


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        n1=1
        n2=2
        for i in range(1,n+1):

            if i==1:
                sum=1
            elif i==2:
                sum=2
            else:
                sum=n1+n2
                n1=n2
                n2=sum
        return sum

if __name__ == "__main__":
    r = Solution().climbStairs2(4)
    print r