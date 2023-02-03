"""
描述
将一个节点数为 size 链表 m 位置到 n 位置之间的区间反转，要求时间复杂度
O(n)，空间复杂度 O(1)。
例如：
给出的链表为 1→2→3→4→5→NULL, m=2,n=4,
返回
1→4→3→2→5→NULL.
数据范围： 链表长度  0<size≤1000，
0<m≤n≤size，链表中每个节点的值满足 ∣val∣≤1000
要求：时间复杂度 O(n) ，空间复杂度 O(n)
进阶：时间复杂度 O(n)，空间复杂度 O(1)
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#
class Solution:
    def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:
        # write code here
        if not head or head.next:
            return head
         