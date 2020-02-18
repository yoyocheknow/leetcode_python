# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 这道题要求使用固定空间。所以先遍历整个链表然后放在一个list中排序，再链接起来这种方法就不考虑了。
    # 下面的思路是，把这个链表分为两个有序链表，然后merge这两个有序链表即可。那么怎么让每个链表有序呢？
    # 使用递归的方式来做，当递归到链表只剩两个节点时，比较这两个节点，然后排序。
    # 当第一次merge链表时，这两个有序链表都不超过2个节点，merge一次就会使4个节点有序，然后使原始两个链表有序。
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype
        """
        if not head:
            return head
        if not head.next:
            return head
        if not head.next.next:
            if head.val>head.next.val:
                temp=head

                head=head.next
                temp.next=None
                head.next=temp
            return head

        slow,fast=head,head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next

        right=slow.next
        slow.next=None

        temp1=self.sortList(head)
        temp2=self.sortList(right)

        return self.mergeList(temp1,temp2)

    def mergeList(self,head1,head2):
        if not head1:
            return
        if not head2:
            return

        if head2.val<head1.val:
            node=head2
            head2=head2.next
        else:
            node=head1
            head1=head1.next
        dummy=node
        while(head1 and head2):
            if head1.val<head2.val:
                node.next=head1
                node=node.next
                head1=head1.next
            else:
                node.next = head2
                node = node.next
                head2 = head2.next

        if head1:
            node.next=head1
        if head2:
            node.next=head2

        return dummy


if __name__ == "__main__":

    L5 = ListNode(5)
    L4 = ListNode(3)
    L3 = ListNode(1)
    L2 = ListNode(2)
    L1 = ListNode(4)
    L1.next = L2
    L2.next = L3
    L3.next = L4
    L4.next = L5
    r = Solution().sortList(L1)
    while (r):
        print r.val
        r = r.next
