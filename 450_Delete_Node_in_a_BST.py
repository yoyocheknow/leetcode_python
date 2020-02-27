# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 删除的节点分为以下几种情况：
    # 1-删除的叶子节点，那么直接将此节点删除即可。即，此节点的父节点的左指针或者右指针为空
    # 2-删除的节点只有左子树或者只有右子树，那么就将此节点的父节点指向起左子树或者右子树即可。
    # 3-删除的节点既有左子树又有右子树，那么就应该让此节点的后继节点替换此节点的值，然后删除后继节点。
    #   后继节点是指大于此节点值中具有最小值的节点，若此节点的右子树非空，那么它的后继节点是右子树中最左侧的节点。
    #   另外也隐含了，此节点最多只有一个子树，所以删除后继节点时，按照情况2进行删除即可。
    parent=None
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        node=self.BST_search(root,key)
        if not node:
            return root
        if node.left and node.right:
            successor = self.find_successor(node)
            self.delete_node(successor)
            node.val=successor.val
            return root
        if self.parent:
            self.delete_node(node)
            return root
        if node.left:
            root=node.left
        else:
            root=node.right
        return root
    def find_successor(self,node):
        self.parent=node
        ptr = node.right
        while(ptr.left):
            self.parent=ptr
            ptr=ptr.left
        return ptr

    def BST_search(self,node,value):
        while node:
            if node.val==value:
                break
            self.parent = node
            if value<node.val:
                node=node.left
            else:
                node=node.right
        return node

    def delete_node(self,node):
        if node.val<self.parent.val:
            if node.left and not node.right:
                self.parent.left=node.left
            elif not node.left and node.right:
                self.parent.left=node.right
            else:
                self.parent.left=None
        elif node.val>self.parent.val:
            if node.left and not node.right:
                self.parent.right=node.left
            elif not node.left and node.right:
                self.parent.right=node.right
            else:
                self.parent.right=None

    def deleteNode2(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        return self.dfs(root, key, None)

    def dfs(self, node, key, l):
        if not node:
            node = l  # l is the left of target node. if we cannot find target node, l is None.
            return node
        if node.val == key:
            l = node.left  #
            return self.dfs(node.right, key, l)  # we delete node and return node.right
        if node.val < key:
            node.right = self.dfs(node.right, key, l)
            return node
        if node.val > key:
            node.left = self.dfs(node.left, key, l)
            return node

if __name__ == "__main__":
    node1 = TreeNode(5)
    node2= TreeNode(3)
    node3 = TreeNode(6)
    node4 = TreeNode(2)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    node1.left=node2
    node1.right=node3
    node2.left = node4
    node2.right=node5
    node3.right=node6
    r = Solution().deleteNode2(node1,3)
    print r