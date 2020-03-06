# -*- coding:utf-8 -*-


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def backtrack(nums,arr1):
            if len(nums)==0:
                if arr1 not in res:
                    res.append(arr1)
                    return

            for i in range(len(nums)):
                curr=nums[i]
                others=nums[:i]+nums[i+1:]
                backtrack(others,arr1+[curr])

        backtrack(nums,[])

        return res

if __name__ == "__main__":
    r = Solution().permuteUnique([1,1,2])
    print r