# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack=[]
        res=0
        if root:
            stack.append(root)
        while(stack):
            for i in range(len(stack)):
                node=stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res += 1

        return res
    #递归解法
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        left_depth=self.maxDepth1(root.left)
        right_depth=self.maxDepth1(root.right)
        max=left_depth if left_depth>right_depth else right_depth
        max += 1
        return max

if __name__ == "__main__":
    node1=TreeNode(3)
    node2=TreeNode(9)
    node3=TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node6 = TreeNode(2)
    node7 = TreeNode(3)

    node1.left=node2
    node1.right = node3
    # node2.left = node4
    # node2.right = node5
    node3.left = node4
    node3.right = node5

    r=Solution().maxDepth1(node1)

    print r
