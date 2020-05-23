"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

递归也可以。
l1.next = merge(l1.next, l2)
或者
l2.next = merge(l1, l2.next)
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        cur = head
        while l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            cur.next = node
            cur = node

        while l1:
            node = ListNode(l1.val)
            cur.next = node
            cur = node
            l1 = l1.next

        while l2:
            node = ListNode(l2.val)
            cur.next = node
            cur = node
            l2 = l2.next

        return head.next
