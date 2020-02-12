# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.max_sum = float('-inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def recusive(root):

            if not root:
                return 0
            l,r=0,0
            if root.left:
                l=recusive(root.left)
            if root.right:
                r=recusive(root.right)
            # max_sum保存遍历途中的最大值
            self.max_sum=max(self.max_sum,l+root.val,r+root.val,l+root.val+r,root.val)
            # 下面的return中都包含了root，是因为，只要想往上走，必须包含root这个路径，最大值已经保存在max_sum中。所以不必返回max_sum
            return max(root.val,max(l,r)+root.val)

        recusive(root)
        return self.max_sum

if __name__ == "__main__":
    node1=TreeNode(-3)
    node2=TreeNode(-2)
    node3=TreeNode(-3)
    node4 = TreeNode(1)
    node5 = TreeNode(3)
    node6 = TreeNode(-2)
    node7 = TreeNode(-1)

    # node1.left=node2
    # node1.right = node3
    # node2.left = node4
    # node2.right = node5
    # node3.left = node6
    # node4.right = node7

    r=Solution().maxPathSum(node1)

    print r
