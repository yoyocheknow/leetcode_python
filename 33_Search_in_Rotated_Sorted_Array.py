# -*- coding:utf-8 -*-

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left =0
        right = len(nums)-1
        while(left<=right):
            mid = (left+right)/2
            if target == nums[mid]:
                return mid
            # right half is sorted
            if nums[mid]<=nums[right]:
                if nums[mid]<target and target<=nums[right]:
                    left=mid+1
                else:
                    right = mid-1
            # left half is sorted
            else:
                if nums[left]<=target and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1

        return -1
if __name__ == "__main__":
    r = Solution().search([4,5,6,7,0,1,2],0)
    print r
