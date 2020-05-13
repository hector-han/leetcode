"""
合并二叉树
easy

给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

"""
from utils import TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        left1, left2 = None, None
        right1, right2 = None, None
        val = 0
        if t1 is None:
            if t2 is None:
                return None
            else:
                val = t2.val
                left2 = t2.left
                right2 = t2.right
        else:
            left1 = t1.left
            right1 = t1.right
            val = t1.val
            if t2:
                val += t2.val
                left2 = t2.left
                right2 = t2.right

        new_root = TreeNode(val)
        left = self.mergeTrees(left1, left2)
        right = self.mergeTrees(right1, right2)
        new_root.left = left
        new_root.right = right
        return new_root

if __name__ == '__main__':
    pass