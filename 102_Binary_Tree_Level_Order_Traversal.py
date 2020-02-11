# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack=[]
        res_list=[]
        if root:
            stack.append(root)
        while(stack):
            temp=[]
            for i in range(len(stack)):
                node = stack[0]
                stack.pop(0)
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            res_list.append(temp)

        return res_list

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

    r=Solution().levelOrder(node1)

    print r