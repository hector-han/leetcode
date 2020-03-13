"""
反转一个单链表
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        pre = None
        cur = head
        nex = cur.next
        while nex is not None:
            cur.next = pre
            pre = cur
            cur = nex
            nex = cur.next
        cur.next = pre
        return cur
