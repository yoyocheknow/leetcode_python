# -*- coding:utf-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i=0

        max_income=0
        while(i<len(prices)-1):
            while(i<len(prices)-1 and prices[i]>=prices[i+1]):
                i+=1
            vally=prices[i]
            while(i<len(prices)-1 and prices[i]<=prices[i+1]):
                i+=1
            peak=prices[i]
            max_income+=peak-vally

        return max_income

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_income=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                max_income += prices[i]-prices[i-1]

        return max_income


if __name__ == "__main__":

    r=Solution().maxProfit2([7,1,5,3,6,4])
    print r
