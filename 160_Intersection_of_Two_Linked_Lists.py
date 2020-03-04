
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 思路是先让两个链表的头部对齐，然后一起往下走，如果有交点那么必定会指向同一个节点。
        lengthA,lengthB=0,0
        h1=headA
        h2=headB
        while(h1):
            h1=h1.next
            lengthA+=1
        while(h2):
            h2=h2.next
            lengthB+=1
        diff=abs(lengthA- lengthB )
        if lengthA>lengthB:
            while(diff>0):
                headA=headA.next
                diff-=1
        else:
            while (diff > 0):
                headB = headB.next
                diff -= 1
        #现在headA和headB处于同一起跑线上
        while(headA and headB):
            if headA!=headB:
                headA=headA.next
                headB=headB.next
            else:
                return headA
        return None
if __name__ == "__main__":
    L5 = ListNode(5)
    L4 = ListNode(4)
    L3 = ListNode(8)
    L2 = ListNode(1)
    L1 = ListNode(4)
    L1.next = L2
    L2.next = L3
    L3.next = L4
    L4.next = L5

    LB3 = ListNode(1)
    LB2 = ListNode(0)
    LB1 = ListNode(5)
    LB1.next=LB2
    LB2.next=LB3
    LB3.next=L3
    r = Solution().getIntersectionNode(L1,LB1)

    print r.val