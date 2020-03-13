"""
编写一个程序，找到两个单链表相交的起始节点。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        p1 = headA
        p2 = headB
        while p1 != p2:
            if p1 is None:
                p1 = headB
                p2 = p2.next
                continue
            if p2 is None:
                p2 = headA
                p1 = p1.next
                continue
            p1 = p1.next
            p2 = p2.next
        return p1

if __name__ == '__main__':
    def build(a):
        head = ListNode(0)
        cur = head
        for v in a:
            cur.next = ListNode(v)
            cur = cur.next
        return head.next
    ha = build([0])
    hb = build([1, 3])
    sol = Solution()
    ret = sol.getIntersectionNode(ha, hb)
    print(ret)