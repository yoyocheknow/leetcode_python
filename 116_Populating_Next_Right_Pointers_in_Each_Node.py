# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        stack=[]
        if root:
            stack.append(root)
        while(stack):
            temp = []
            for i in range(len(stack)):
                node=stack.pop(0)
                temp.append(node)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            for j in range(len(temp)-1):
                temp[j].next=temp[j+1]

        return root

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    r=Solution().connect(node1)
    def printTree(root):
        while(root):
            print root.val,root.next
            if root.left:
                printTree(root.left)
            if root.right:
                printTree(root.right)
            return

    printTree(r)
