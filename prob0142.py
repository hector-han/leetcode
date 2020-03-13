"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        head_cache = head
        while fast is not None:
            if fast.next is None:
                return None
            else:
                fast = fast.next.next
                if fast is None:
                    return None
                slow = slow.next
            if fast == slow:
                break
        while head_cache != slow:
            head_cache = head_cache.next
            slow = slow.next
        return slow
