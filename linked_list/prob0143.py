"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
"""

from utils import ListNode, print_link_list, create_link_list


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # step 1, split to 2 list
        nums = 0
        node = head
        while node:
            nums += 1
            node = node.next

        if nums < 3:
            return

        head2 = head
        mid_idx = (nums + 1) // 2
        n = 0
        while n < mid_idx:
            if n == mid_idx - 1:
                tmp = head2.next
                head2.next = None
                head2 = tmp
            else:
                head2 = head2.next
            n += 1

        # step 2, reverse part 2
        node = None
        while head2:
            tmp = head2.next
            head2.next = node
            node = head2
            head2 = tmp
        head2 = node

        # step 3, concatenate head and head2
        node1, node2 = head, head2
        while node2:
            tmp = node1.next
            node1.next = node2
            node2 = tmp
            node1 = node1.next


if __name__ == '__main__':
    link_list = create_link_list([1,2,3,4,5])
    sol = Solution()
    sol.reorderList(link_list)
    print_link_list(link_list)


        




