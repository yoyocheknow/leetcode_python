# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head=ListNode(0)
        last_head = ListNode(0)
        if head and head.next:
            new_head=head.next
        else:
            return head
        while(head and head.next):
            # 保存第二个节点的next
            temp = head.next.next
            next_node = head.next
            next_node.next=head
            # last_head用来保存1->4这个节点的关系，就是上一步循环中的头部，指向新的循环的头部
            if last_head:
                last_head.next= next_node
            head.next=temp
            last_head = head
            head=next_node.next.next
        return new_head

if __name__ == "__main__":

    L5 = ListNode(5)
    L4 = ListNode(4)
    L3 = ListNode(3)
    L2 = ListNode(2)
    L1 = ListNode(1)
    L1.next = L2
    L2.next = L3
    L3.next = L4
    # L4.next = L5
    r = Solution().swapPairs(L1)
    while (r):
        print r.val
        r = r.next
