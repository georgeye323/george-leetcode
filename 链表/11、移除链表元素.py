"""
leetcode 203
题意：删除链表中等于给定值 val 的所有节点。

示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

示例 2：
输入：head = [], val = 1
输出：[]

示例 3：
输入：head = [7,7,7,7], val = 7
输出：[]
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solution(list_node: ListNode, val: int):
    # 设置虚拟节点
    pump = ListNode(next=list_node)
    cur = pump
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return pump


