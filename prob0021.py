# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        cur = head
        while l1.next and l2. next:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            cur.next = node
            cur = node

        while l1.next:
            node = ListNode(l1.val)
            cur.next = node
            cur = node
            l1 = l1.next

        while l2.next:
            node = ListNode(l2.val)
            cur.next = node
            cur = node
            l2 = l2.next

        return head.next
