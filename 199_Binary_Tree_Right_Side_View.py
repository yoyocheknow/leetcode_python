
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        res=[]
        if not root:
            return res
        stack.append(root)
        while(stack):
            res.append(stack[-1].val)
            for i in range(len(stack)):
                node = stack[0]
                stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return res

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2= TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(5)
    node5 = TreeNode(4)
    node1.left=node2
    node1.right=node3
    node2.right=node4
    node3.right=node5
    r = Solution().rightSideView(node1)
    print r