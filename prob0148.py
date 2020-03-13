"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
类似归并排序
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        num_of_nodes = 0
        cur = head
        while cur is not None:
            num_of_nodes += 1
            cur = cur.next
        if num_of_nodes < 2:
            return head

        def merge(l1: ListNode, l2: ListNode):
            """
            合并两个listnode
            """
            head = ListNode(0)
            cur = head
            while l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1 is not None:
                cur.next = l1
            else:
                cur.next = l2
            return head.next

        step = num_of_nodes // 2
        l1 = head
        l2 = head
        while step - 1 > 0:
            l2 = l2.next
            step -= 1
        cache = l2
        l2 = l2.next
        cache.next = None
        return merge(self.sortList(l1), self.sortList(l2))


if __name__ == '__main__':
    def my_print(head):
        str_ret = ''
        while head is not None:
            str_ret += '{}->'.format(head.val)
            head = head.next
        print(str_ret)
    head = ListNode(0)
    cur = head
    import random
    nums = [random.randint(0, 30) for i in range(10)]
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    my_print(head)
    sol = Solution()
    my_print(sol.sortList(head))





