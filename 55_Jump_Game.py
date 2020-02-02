# -*- coding:utf-8 -*-


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #dp[i]代表nums[i]最远到达的位置
        if len(nums)==1:
            return True
        dp=[0]*(len(nums)-1)
        dp[0]=nums[0]
        for i in range(1,len(nums)-1):
            if dp[i-1]<i:
                return False
            elif dp[i-1]<=nums[i]+i:
                dp[i]=nums[i]+i
            else:
                dp[i]=dp[i-1]
            if dp[i]>=len(nums)-1:
                return True
        for j in range(len(dp)):
            if dp[j] >=len(nums)-1:
                return True
        return False

if __name__ == "__main__":
    r = Solution().canJump([1,2])
    print r
