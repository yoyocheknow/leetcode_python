# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        slow = fast = cur = ListNode(0)
        cur.next = head

        # move fast pointer 'n' steps ahead
        for _ in range(n):
            fast = fast.next

        # now move slow and fast pointers in tandem
        while fast.next:
            fast = fast.next
            slow = slow.next

        # now slow is at (n+1)th node
        slow.next = slow.next.next
        return cur.next

if __name__ == "__main__":

    L5 = ListNode(5)

    # L4 = ListNode(4)
    # L4.next=L5
    L3 = ListNode(3)
    # L3.next=L4
    L2 = ListNode(2)
    L2.next=L3
    L1 = ListNode(1)
    L1.next=L2
    r = Solution().removeNthFromEnd(L1,2)
    while(r):
        print r.val
        r=r.next
