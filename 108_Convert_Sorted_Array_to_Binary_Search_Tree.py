# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(begin,end):
            if begin<=end and begin>=0 and end<len(nums):
                mid =(begin+end)/2
                node=TreeNode(nums[mid])
                node.left=helper(begin,mid-1)
                node.right=helper(mid+1,end)
                return node
            else:
                return
        return helper(0,len(nums)-1)

if __name__ == "__main__":

    r = Solution().sortedArrayToBST([-10,-3,0,5,9])
    print r
