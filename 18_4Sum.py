# -*- coding:utf-8 -*-


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result =set()
        nums.sort()
        length = len(nums)
        for i in range(length-3):
            for j in range(i+1,length-2):
                left = j+1
                right = length-1
                diff = target-nums[i]-nums[j]
                while(left<right):
                    sum = nums[left]+nums[right]
                    if sum == diff:
                        result.add(tuple([nums[i],nums[j],nums[left],nums[right]]))
                        right -=1
                    elif sum>diff:
                        right -=1
                    else:
                        left +=1

        return result

if __name__ == "__main__":
    r = Solution().fourSum([1, 0, -1, 0, -2, 2],0)
    print r