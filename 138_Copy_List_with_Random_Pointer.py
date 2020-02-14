# -*- coding:utf-8 -*-

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def __init__(self):
        self.map={}
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 通过一个字典来存放遍历过的node，便于给random赋值
        if not head:
            return
        elif self.map.get(hash(head)):
            return self.map.get(hash(head))
        else:
            new_node = Node(0)
            self.map[hash(head)]=new_node
            new_node.val=head.val
            new_node.next=self.copyRandomList(head.next)
            new_node.random = self.copyRandomList(head.random)
            return new_node


if __name__ == "__main__":
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    node5.next=None

    node1.random=None
    node2.random=node1
    node3.random = node5
    node4.random = node3
    node5.random = node1
    r = Solution().copyRandomList(node1)

    while r:
        print r.val,r.next,r.random
        r=r.next
    print r