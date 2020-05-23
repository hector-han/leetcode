"""
删除链表的倒数第N个节点

给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        m = 0
        node = head
        while node:
            m += 1
            node = node.next
        delete_idx = m - n
        if delete_idx == 0:
            return head.next
        idx = 0
        node = head
        previous = None
        while idx < delete_idx:
            idx += 1
            previous = node
            node = node.next
        previous.next = node.next
        return head


