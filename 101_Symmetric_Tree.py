# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_mirror(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return root1.val==root2.val and \
                   is_mirror(root1.left,root2.right) and \
                   is_mirror(root1.right,root2.left)

        return is_mirror(root,root)

if __name__ == "__main__":
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(2)
    node4 = TreeNode(2)
    node5 = TreeNode(2)
    node6 = TreeNode(2)
    node7 = TreeNode(3)

    node1.left=node2
    node1.right = node3
    node2.left = node4
    # node2.right = node5
    node3.left = node6
    # node3.right = node7

    r=Solution().isSymmetric(node1)

    print r