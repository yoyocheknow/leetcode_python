# -*- coding:utf-8 -*-
import copy

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def recurse(nums, arr1, arr2):

            if len(nums) == 0:
                return arr2.append(arr1)

            for i in range(len(nums)):
                curr = nums[i]
                others = nums[:i] + nums[1 + i:]

                recurse(others, arr1 + [curr], arr2)

        arr2 = []
        recurse(nums, [], arr2)

        return arr2


if __name__ == "__main__":
    r = Solution().permute([1,2,3])
    print r