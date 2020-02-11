# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 按照中序遍历的思想做，二叉搜索树中序遍历一定是有序的，所以在这个遍历的过程中去做判断
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        inorder_list=[]

        def inorder(root):
            res_left,res_right=True,True
            if root.left:
                res_left=inorder(root.left)
            if len(inorder_list)>=1 and root.val<=inorder_list[-1]:
                return False
            inorder_list.append(root.val)
            if root.right:
                res_right=inorder(root.right)
            return res_left and res_right
        return inorder(root)

if __name__ == "__main__":
    node1=TreeNode(10)
    node2=TreeNode(5)
    node3=TreeNode(15)
    node4 = TreeNode(6)
    node5 = TreeNode(20)
    node6 = TreeNode(6)
    node1.right=node3
    node1.left=node2
    node3.right = node5
    node3.left = node4

    r=Solution().isValidBST(node1)

    print r