# -*- coding:utf-8 -*-


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 使用异或的思想
        # a^0=a
        # a^a=0
        # a^b^a=(a^a)^b=0^b=b
        a = 0
        for i in nums:
            a ^= i
        return a

if __name__ == "__main__":

    r = Solution().singleNumber([4,1,2,1,2])
    print r