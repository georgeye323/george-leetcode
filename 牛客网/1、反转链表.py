"""
描述
给定一个单链表的头结点pHead(该头节点是有值的，比如在下图，它的val是1)，长度为n，反转该链表后，返回新链表的表头。

数据范围：0≤n≤1000

要求：空间复杂度 O(1) ，时间复杂度 O(n) 。
如当输入链表{1,2,3}时，
经反转后，原链表变为{3,2,1}，所以对应的输出为{3,2,1}。
以上转换过程如下图所示：
https://uploadfiles.nowcoder.com/images/20211014/423483716_1634206291971/4A47A0DB6E60853DEDFCFDF08A5CA249
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        """
           解法一：利用双指针解决
            if not head:
                return head
            pre = None
            cur = head
            while cur:
				# 临时保存下一节点
                temp = cur.next
				# 当前的next指向前一个
                cur.next = pre
				# 前一个更新为当前
                pre = cur
				# 当前为下一节点
                cur = temp
            return pre
           解法二：利用递归(递归三部曲)
				1、找整个递归的终止条件：递归应该在什么时候结束？
				2、找返回值：应该给上一级返回什么信息？
				3、本级递归应该做什么：在这一级递归中，应该完成什么任务？
        """
        if head is None or head.next is None:
            return head
        pump = self.ReverseList(head.next)
        head.next.next = head
        head.next = None
        return pump