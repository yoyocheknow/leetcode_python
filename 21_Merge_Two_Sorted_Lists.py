# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res_head=res_list=ListNode(0)

        while(l1 and l2):
           if l1.val<l2.val:
               res_list.next = l1
               l1=l1.next
               res_list=res_list.next
           else:
               res_list.next = l2
               l2=l2.next
               res_list = res_list.next
        while(l1):
            res_list.next=l1
            l1=l1.next
            res_list = res_list.next
        while(l2):
            res_list.next=l2
            l2=l2.next
            res_list = res_list.next

        return res_head.next


if __name__ == "__main__":

    L5 = ListNode(5)

    L4 = ListNode(4)
    L4.next=L5
    L3 = ListNode(3)
    L3.next=L4
    L2 = ListNode(2)
    L2.next=L3
    L1 = ListNode(1)
    L1.next=L2

    R1 = ListNode(1)
    R2 = ListNode(3)
    R3 = ListNode(4)
    R1.next=R2
    R2.next=R3
    r = Solution().mergeTwoLists(L1,R1)
    while(r):
        print r.val
        r=r.next
