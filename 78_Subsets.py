# -*- coding:utf-8 -*-
import copy
class Solution(object):
    # 递归
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        output = [[]]
        for num in nums:
            temp=[]
            for curr in output:
                temp+=[curr+[num]]
            output+=temp
            # output += [curr + [num] for curr in output]

        return output
    #回溯
    def subsets1(self, nums):
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
    #二进制法
    def subsets3(self, nums):
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output

if __name__ == "__main__":
    r = Solution().subsets3([1,2,3])
    print r