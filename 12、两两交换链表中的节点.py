"""
leetcode 24
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solution(head: ListNode):
    # 定义虚拟节点
    pump = ListNode(val=0, next=head)
    pre = pump
    while pre.next and pre.next.next:
        # 交换两个节点
        cur = pre.next
        post = pre.next.next

        cur.next = post.next
        post.next = cur
        pre.next = post

        pre = pre.next.next
    return pump.next

def solution1(head: ListNode):
    # 递归
    if not head or not head.next:
        return head
    else:
        new_node = head.next
        head.next = solution1(new_node.next)
        new_node.next = head
        return new_node
