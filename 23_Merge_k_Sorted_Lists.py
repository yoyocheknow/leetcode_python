# -*- coding:utf-8 -*-
import sys
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 挨个遍历每一个list Compare one by one。时间复杂度：O(kN)，k是k个list，N是node节点个数，空间复杂度o(N)
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        res_list = res_head =ListNode(0)
        min_index=0
        while(True):
            is_break=True
            min =sys.maxint
            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val <= min:
                        min = lists[i].val
                        min_index = i
                    is_break = False

            if is_break:
                break
            res_list.next=lists[min_index]
            res_list = res_list.next
            lists[min_index] = lists[min_index].next

        res_list.next=None
        return res_head.next

    # 借助sort函数，把所有节点放在list里，然后sort排序，再生成链表。时间复杂度：O(NlogN)，空间复杂度：O(N)
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


if __name__ == "__main__":

    L5 = ListNode(5)
    L4 = ListNode(4)
    L1 = ListNode(1)
    L4.next = L5
    L1.next=L4

    R1 = ListNode(1)
    R2 = ListNode(3)
    R3 = ListNode(4)
    R1.next=R2
    R2.next=R3

    T1 = ListNode(2)
    T2 = ListNode(6)
    T1.next = T2


    list=[L1,R1,T1]
    r = Solution().mergeKLists(list)
    while(r):
        print r.val
        r=r.next