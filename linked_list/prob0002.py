"""
两数相加
medium

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        level = 0
        head = ListNode(0)
        previous = head
        while l1 and l2:
            val = l1.val + l2.val + level
            level = val // 10
            val = val % 10

            node = ListNode(val)
            previous.next = node
            previous = node
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val + level
            level = val // 10
            val = val % 10

            node = ListNode(val)
            previous.next = node
            previous = node
            l1 = l1.next

        while l2:
            val = l2.val + level
            level = val // 10
            val = val % 10
            node = ListNode(val)
            previous.next = node
            previous = node
            l2 = l2.next
        if level > 0:
            node = ListNode(level)
            previous.next = node

        return head.next