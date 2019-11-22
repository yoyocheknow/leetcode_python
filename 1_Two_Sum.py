
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        h={}
        for i,n in enumerate(nums):
            temp = nums[i]
            diff = target-temp
            if diff not in h:
                h[temp]=i
            else:
                return [h[diff],i]
