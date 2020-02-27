# -*- coding:utf-8 -*-

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[]
        item=[]
        nums.sort()
        output.append(item)
        def backtrack(i,item):
            if i>=len(nums):
                return
            item.append(nums[i])
            if item not in output:
                output.append(item)
            backtrack(i+1,item[:])
            backtrack(i+1,item[:-1])

        backtrack(0,[])
        return output

if __name__ == "__main__":
    r = Solution().subsetsWithDup([1,2,2])
    print r