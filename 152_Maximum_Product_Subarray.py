# -*- coding:utf-8 -*-


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int] 
        :rtype: int
        """
        #记录一个最大正数和一个最小负数，每次取nums[i]和nums[i]*最大正数，nums[i]*最小负数中最大的那一个
        #因为记录最小负数，如果nums[i]为负数，那么nums[i]*最小负数就有可能成为最大的那一个
        ans=most_negative=most_positive=nums[0]
        for i in range(1,len(nums)):
            candidates = (nums[i], most_negative * nums[i], most_positive * nums[i])

            most_positive=max(candidates)
            most_negative=min(candidates)
            ans=max(ans,most_positive)
        return ans


if __name__ == "__main__":
    r = Solution().maxProduct([-2,3,5,-4,-1])

    print r