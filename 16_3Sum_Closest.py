# -*- coding:utf-8 -*-


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = abs(nums[0]+nums[1]+nums[2]-target)
        res=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-1):
            left = i+1
            right = len(nums)-1
            while(left<right):
                sum = nums[i]+nums[left]+nums[right]
                if abs(sum - target)<diff:
                    res = sum
                    diff = abs(sum - target)
                if sum>target:
                    right -=1
                else:
                    left+=1

        return res


if __name__ == "__main__":
    r = Solution().threeSumClosest([0,2,1,-3], 1)
    print r
