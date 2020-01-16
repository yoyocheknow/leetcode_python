# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # new_head记录第一个k翻转后的头部
    new_head = ListNode(0)
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n,m=k,k
        # 先把头节点找到
        new_head = head
        while(m>1 and new_head):
            new_head = new_head.next
            m-=1
        self.new_head=new_head if new_head else head

        # 翻转k个节点
        def reverse(head,n):
            cur,pre=head,None
            while(n>0 and head):
                temp=cur.next
                cur.next=pre
                pre=cur
                cur=temp
                n-=1
            return head, cur, pre
        # 看是否满足k个长度来翻转
        def try_k(head,n):
            while(head and n>0):
                head=head.next
                n-=1

            if n ==0:
                return True
            else:
                return False

        last_tail=None
        while (try_k(head, n)):
            # current_tail翻转k个节点后的 尾部
            # current_head翻转k个节点后的 头部
            # next_head 下一次翻转前的头部
            current_tail, next_head,current_head= reverse(head, n)
            print current_head.val ,current_tail.val, next_head.val
            if last_tail:
                # 如果有上一步翻转后的尾部，那么上一次翻转后的尾部 next指向本次翻转后的头部
                last_tail.next = current_head
            last_tail = current_tail
            # current_tail.next 指向下一次翻转前的头部（如果没有下一次翻转），如果还有下一次翻转的话，上面的if last_tail 就会更新
            current_tail.next = next_head
            head = next_head



        return self.new_head

if __name__ == "__main__":

    L5 = ListNode(5)
    L4 = ListNode(4)
    L3 = ListNode(3)
    L2 = ListNode(2)
    L1 = ListNode(1)
    L1.next = L2
    L2.next = L3
    L3.next = L4
    L4.next = L5
    r = Solution().reverseKGroup(L1,2)
    while (r):
        print r.val
        r = r.next
