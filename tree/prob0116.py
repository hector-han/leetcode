"""
填充每个节点的下一个右侧节点指针
和117类似，但比117简单。 116是117的特例，会117即可
medium

给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        leftmost = root
        while leftmost:
            cur = leftmost
            leftmost = None
            pre = None
            while cur:
                if cur.left is None:
                    # tree finished
                    return root
                if not leftmost:
                    leftmost = cur.left
                    cur.left.next = cur.right
                    pre = cur.right
                else:
                    pre.next = cur.left
                    pre = pre.next
                    pre.next = cur.right
                    pre = cur.right
                cur = cur.next
        return root

