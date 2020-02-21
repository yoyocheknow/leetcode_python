class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        index = -1
        start = 0
        end = len(nums) - 1

        while (index == -1):
            mid = (end + start) / 2
            if target == nums[mid]:
                index = mid
            elif target < nums[mid]:
                if mid == 0 or target > nums[mid - 1]:
                    index = mid
                end = mid - 1
            else:
                if mid == len(nums) - 1 or target < nums[mid + 1]:
                    index = mid + 1
                start = mid + 1

        return index