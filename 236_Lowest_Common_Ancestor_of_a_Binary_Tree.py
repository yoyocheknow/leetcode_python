# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        res=[]
        def dfs(root,search, path,finish):
            if not root or finish:
                return
            path.append(root.val)
            if root ==search:
                finish=1
                res.append(path)
            dfs(root.left,search,path[:],finish)
            dfs(root.right,search,path[:],finish)
        dfs(root,p,[],0)
        l1=res[0]
        res.pop()
        dfs(root, q, [], 0)
        l2=res[0]
        i,j=0,0
        print l1,l2
        ancestor=None
        while(i<len(l1) and j<len(l2)):
            if l1[i]==l2[j]:
                ancestor = l1[i]
                i+=1
                j+=1
            else:
                return ancestor
        return ancestor


if __name__ == "__main__":
    node1=TreeNode(3)
    node2=TreeNode(5)
    node3=TreeNode(1)
    node4 = TreeNode(6)
    node5 = TreeNode(2)
    node6 = TreeNode(0)
    node7 = TreeNode(8)
    node8 = TreeNode(7)
    node9 = TreeNode(4)

    node1.left=node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    node3.left = node6
    node3.right = node7

    node5.left=node8
    node5.right=node9


    r=Solution().lowestCommonAncestor(node1,node2,node9)

    print r

