# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 递归写法
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res_list = []
        if not root:
            return
        def inorder(root):
            if root.left:
                inorder(root.left)
            if root:
                res_list.append(root.val)
            if root.right:
                inorder(root.right)
            return

        inorder(root)
        return res_list

    # 迭代写法
    def inorderiterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res_list = []
        stack=[]
        while(len(stack)!=0 or root):
            while(root):
                stack.append(root)
                root=root.left
            if len(stack)!=0:
                root=stack.pop()
                res_list.append(root.val)
                root=root.right


        return res_list

if __name__ == "__main__":
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node1.right=node2
    node2.left=node3
    r=Solution().inorderiterative(node1)

    print r