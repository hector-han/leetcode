
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        O(n)空间复杂度的方法，想象两个人在操场跑步，如果速度不同，终会相遇。
        :param head:
        :return:
        """
        id_set = set()
        cur = head
        while cur is not None:
            cur_id = id(cur)
            if cur_id in id_set:
                return True
            id_set.add(cur_id)
            cur = cur.next
        return False