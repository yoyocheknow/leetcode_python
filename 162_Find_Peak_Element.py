# -*- coding:utf-8 -*-

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # o(n)的时间复杂度
        if len(nums)<2:
            return 0
        if len(nums)<3:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        nums.append(float('-inf'))
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
        return 0

    # o(logn)的时间复杂度
    def findPeakElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high=0,len(nums)-1
        while(low<high):
            mid=low + int((high-low)/2)
            if nums[mid]>nums[mid+1]:
                high=mid
            else:
                low=mid+1
        return low

if __name__ == "__main__":
    r = Solution().findPeakElement1([1,2,1,3,5,6,4])

    print r