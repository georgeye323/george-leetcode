"""
leetcode 206
题意：反转一个单链表。

示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL
"""
class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self, head:ListNode):
        # 定义一个虚拟节点
        if not head:
            return None
        cur = head
        pre = None
        while cur:
            # 断开头结点
            temp = cur.next
            # 头结点指向前一节点
            cur.next = pre
            # 指针后移
            pre = cur
            cur = temp
        return pre

    def ReverseList1(self, head:ListNode):
        # 递归的解法
        if not head or not head.next:
            return head
        # 反转下一节点
        pump = self.ReverseList(head.next)
        head.next.next = head
        # 此时的head在最后面，需要指向空
        head.next = None
        return pump

        
            