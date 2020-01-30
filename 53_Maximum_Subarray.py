# -*- coding:utf-8 -*-

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dp用来记录nums[0...i]从0到i最长的子序列之和
        #若dp[i-1]小于0，则dp[i]不用dp[-i]，直接从新的nums[i]开始
        dp=[0]*len(nums)
        dp[0]=nums[0]
        res=dp[0]
        for i in range(1,len(nums)):
            if nums[i]+dp[i-1]>nums[i]:
                dp[i]=nums[i]+dp[i-1]
            else:
                dp[i]=nums[i]
            res = dp[i] if dp[i]>res else res
        print dp
        return res

if __name__ == "__main__":
    r = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print r