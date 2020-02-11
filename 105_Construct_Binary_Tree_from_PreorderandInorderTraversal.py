# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.builtT(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)

    def builtT(self, preorder,prestart,preend, inorder,instart,inend):
        if instart>inend:
            return
        root = TreeNode(preorder[prestart])
        root_position = self.findIndex(inorder, root.val)
        root.left = self.builtT(preorder,prestart+1,prestart+root_position-instart,inorder,instart,root_position-1)
        root.right = self.builtT(preorder,prestart+root_position-instart+1,preend,inorder,root_position+1,inend)
        return root

    def findIndex(self,order,num):
        for i in range(len(order)):
            if order[i]== num:
                return i
        return -1

    # 更优雅的写法，思路和上面的一样
    def buildTree1(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        i = inorder.index(preorder.pop(0))
        root.left = self.buildTree(preorder[:i], inorder[:i])
        root.right = self.buildTree(preorder[i:], inorder[i + 1:])
        return root

if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    r=Solution().buildTree1(preorder,inorder)
    def printTree(root):
        while(root):
            print root.val
            if root.left:
                printTree(root.left)
            if root.right:
                printTree(root.right)
            return

    printTree(r)
