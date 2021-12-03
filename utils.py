

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_link_list(arr):
    head = ListNode(arr[0])
    node = head
    for v in arr[1:]:
        cur = ListNode(v)
        node.next = cur
        node = cur
    return head


def print_link_list(head):
    while head:
        print(head.val)
        head = head.next


def parse_tree(list_val):
    nums = len(list_val)
    nodes = [None] * nums
    nodes[0] = TreeNode(list_val[0])
    for i, v in enumerate(list_val):
        if i == 0:
            continue
        if v is not None:
            nodes[i] = TreeNode(v)
        parent_id = (i-1) // 2
        if nodes[parent_id] is None:
            continue
        if i % 2 == 0:
            nodes[parent_id].right = nodes[i]
        else:
            nodes[parent_id].left = nodes[i]
    return nodes[0]




