"""
Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def find_min(self, list_node):
        min_idx = None
        min_val = None
        for i, l in enumerate(list_node):
            if not l:
                continue
            else:
                if min_idx is None:
                    min_val = l.val
                    min_idx = i
                else:
                    if l.val < min_val:
                        min_val = l.val
                        min_idx = i
        return min_idx

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = [node for node in lists]
        head = ListNode(0)
        cur = head
        idx = self.find_min(nodes)
        while idx is not None:
            node = ListNode(nodes[idx].val)
            cur.next = node
            cur = node
            nodes[idx] = nodes[idx].next
            idx = self.find_min(nodes)
        return head.next


def build_listNode(list_int: List[int]) -> ListNode:
    head = ListNode(0)
    cur = head
    for num in list_int:
        node = ListNode(num)
        cur.next = node
        cur = node
    return head.next


def print_listNode(list_node: ListNode):
    cur = list_node
    while cur:
        print(str(cur.val) + ',', end='')
        cur = cur.next
    print()


if __name__ == '__main__':
    input = [[1,4,5],[1,3,4],[2,6]]
    lists = [build_listNode(v) for v in input]
    solution = Solution()
    ret = solution.mergeKLists(lists)
    print_listNode(ret)


