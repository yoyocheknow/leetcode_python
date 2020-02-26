# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def helper(node):
            if node:
                # DFS travesal to next level
                helper(node.right)
                helper(node.left)

                # flattern binary tree to right skewed linked list
                node.right = self.previous_traversal
                node.left = None
                self.previous_traversal = node

        # record of node of previous traversal
        self.previous_traversal = None
        helper(root)
        return root
if __name__ == "__main__":
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(5)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(6)


    node1.left=node2
    node1.right = node3
    node2.left = node4
    node2.right = node5


    node3.right = node6


    r=Solution().flatten(node1)

    print r



