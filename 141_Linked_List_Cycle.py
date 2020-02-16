# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        first=head.next
        second=head
        while(first and second):
            if first != second:
                if first.next and first.next.next:
                    first=first.next.next
                else:
                    return False

                second=second.next
            else:
                return True

        return False

if __name__ == "__main__":
    L1=ListNode(1)
    L2=ListNode(2)
    L3=ListNode(3)
    L4=ListNode(4)

    # L1.next=L2
    L2.next=L1
    L3.next=L4
    # L4.next=L2
    r = Solution().hasCycle(L1)
    print r