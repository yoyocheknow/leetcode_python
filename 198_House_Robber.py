# -*- coding:utf-8 -*-


class Solution(object):
    # 动态规划问题。dp[i]表示抢劫的房屋最大财宝
    # 动态转移方程：dp[i]=max(dp[i-1],dp[i-2]+nums[i])
    # 含义是指，第i家要么被抢劫，抢劫的话，那么总财宝数是dp[i-2]+nums[i]表示这家被抢劫的财宝加上前i-2家最大的财宝数
    # 第i家不抢劫的话，那么总财宝数是dp[i-1]，表示前i-1家最大的财宝数
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)<2:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[len(nums)-1]