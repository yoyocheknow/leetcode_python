# -*- coding:utf-8 -*-

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        res_first = res
        dif = 0

        while(l1 and l2):
            temp = l1.val + l2.val + dif
            dif = 0
            if temp / 10 > 0:
                dif = temp / 10
                temp = temp % 10
            temp_node = ListNode(temp)
            res.next = temp_node
            res = res.next
            l1 = l1.next
            l2 = l2.next
        while(l1):
            temp = l1.val + dif
            if temp / 10 > 0:
                dif = temp / 10
                temp = temp % 10
            temp_node = ListNode(temp)
            res.next = temp_node
            res = res.next
            l1=l1.next
        while(l2):
            temp = l2.val + dif
            if temp / 10 > 0:
                dif = temp / 10
                temp = temp % 10
            temp_node = ListNode(temp)
            res.next = temp_node
            res = res.next
            l2 = l2.next
        if dif > 0:
            res.next = ListNode(dif)
        return res_first.next



if __name__ == "__main__":
    N1 = ListNode(9)
    N2 = ListNode(9)
    #N3 = ListNode(3)
    N1.next = N2
    # N2.next = N3

    N5 = ListNode(1)
    # N6 = ListNode(6)
    # N7 = ListNode(4)
    # N8 = ListNode(1)
    # N5.next = N6
    # N6.next = N7
    # N7.next = N8
    res = Solution().addTwoNumbers(N1, N5)
    while(res):
        print(res.val)
        res=res.next
    # l=[3,4,5,6]
    # node = Solution().list_to_listnode(l)
    # while(node):
    #     print(node.val)
    #     node = node.next

