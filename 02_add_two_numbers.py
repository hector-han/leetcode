# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        tmp = 0
        cur_node = head
        while l1 and l2:
            digit_sum = tmp + l1.val + l2.val
            tmp = digit_sum // 10
            node = ListNode(digit_sum % 10)
            cur_node.next = node
            cur_node = node
            l1 = l1.next
            l2 = l2.next

        if l2:
            while l2:
                digit_sum = tmp + l2.val
                tmp = digit_sum // 10
                node = ListNode(digit_sum % 10)
                cur_node.next = node
                cur_node = node
                l2 = l2.next
        elif l1:
            while l1:
                digit_sum = tmp + l1.val
                tmp = digit_sum // 10
                node = ListNode(digit_sum % 10)
                cur_node.next = node
                cur_node = node
                l1 = l1.next
        if tmp > 0:
            node = ListNode(tmp)
            cur_node.next = node
        return head.next


if __name__ == '__main__':
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    m1 = ListNode(5)
    m2 = ListNode(6)
    m3 = ListNode(4)
    m1.next = m2
    m2.next = m3

    ret = Solution().addTwoNumbers(n1, m1)
    while ret:
        print(ret.val)
        ret = ret.next

