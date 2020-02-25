# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res=[]
        path=[]
        path_value=0
        def preorder(node,path_value,path):
            if not node:
                return
            path_value +=node.val
            path.append(node.val)
            if not node.left and not node.right and path_value==sum:
                res.append(path)

            preorder(node.left,path_value,path[:])
            preorder(node.right, path_value,path[:])
            path_value-=node.val
        preorder(root,path_value,path)
        return res

if __name__ == "__main__":
    node1=TreeNode(5)
    node2=TreeNode(4)
    node3=TreeNode(8)
    node4 = TreeNode(11)
    node5 = TreeNode(13)
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node8 = TreeNode(2)
    node9 = TreeNode(5)
    node10 = TreeNode(1)
    node1.left=node2
    node1.right = node3
    node2.left = node4

    node3.left = node5
    node3.right = node6
    node4.left = node7
    node4.right = node8

    node6.left=node9
    node6.right=node10


    r=Solution().pathSum(node1,22)

    print r