# -*- coding:utf-8 -*-


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return
        max_income=0
        min_price=prices[0]
        for i in range(1,len(prices)):

            dif=prices[i]-min_price
            min_price=prices[i] if prices[i]<min_price else min_price
            max_income = max_income if max_income>dif else dif
        return max_income


if __name__ == "__main__":

    r=Solution().maxProfit([7,6,4,3,1])
    print r



