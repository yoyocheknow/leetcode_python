# -*- coding:utf-8 -*-

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def right_view(self,root):
        if not root:
            return []
        res=[]
        queue=[]
        queue.append(root)
        while(queue):
            res.append(queue[-1].val)
            for i in range(len(queue)):
                node = queue[0]
                queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2= TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left=node2
    node1.right=node3
    node2.left=node4
    node3.left=node5
    r = Solution().right_view(node1)
    print r