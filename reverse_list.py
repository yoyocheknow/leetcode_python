# -*- coding:utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):     # 迭代
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None

        while cur:
            tmp = cur.next              # 临时列表，用于暂存结果
            cur.next = prev             # 更换连接方向
            prev = cur                  # 后移
            cur = tmp                   # 后移

        return prev

    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:  # 如果输入结点是空，或只有一个结点，返回即可
            return head

        p = self.reverseList1(head.next)  # 将下一个结点之后的部分逆序
        head.next.next = head  # 反转当前结点
        head.next = None  # 设置当前结点的下一个结点为None
        return p

if __name__ == "__main__":

    L5 = ListNode(5)
    L4 = ListNode(4)
    L3 = ListNode(3)
    L2 = ListNode(2)
    L1 = ListNode(1)
    L1.next=L2
    L2.next = L3
    L3.next = L4
    L4.next = L5

    r = Solution().reverseList(L1)
    while(r):
        print r.val
        r=r.next