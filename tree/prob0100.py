"""
相同的树
easy

给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""

from utils import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None:
            if q is None:
                return True
            else:
                return False
        else:
            if q is None:
                return False
            elif q.val != p.val:
                return False
            else:
                f1 = self.isSameTree(p.left, q.left)
                f2 = self.isSameTree(p.right, q.right)
                return f1 and f2
