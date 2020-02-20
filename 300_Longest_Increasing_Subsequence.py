# -*- coding:utf-8 -*-

class Solution(object):
    # dp[i]表示以第i个元素为结尾的最长子序列长度
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        dp =[0]*len(nums)
        dp[0]=1
        max_l=1
        for i in range(1,len(nums)):
            dp[i]=1
            for j in range(i):
                # 如果第i个比前面某一个大，说明第i个元素可以和前面j元素结尾的序列组成上升子序列。当dp[i]<dp[j]+1时，更新dp[i]
                if nums[j]<nums[i] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1

            max_l=max(max_l,dp[i])
        return max_l
    #通过栈来解决
    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        stack=[]
        stack.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]>stack[-1]:
                stack.append(nums[i])
            else:
                for j in range(len(stack)):
                    if stack[j]>=nums[i]:
                        stack[j]=nums[i]
                        break

        return len(stack)

if __name__ == "__main__":

    r = Solution().lengthOfLIS2([10,9,2,5,3,7,101,18])
    print r