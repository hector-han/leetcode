"""
二叉树的直径
easy

给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
"""
from utils import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        递归的求左最长和右最长，同时保存最大值
        """
        if not root:
            return 0

        self.ans = 0
        def _max_path(node: TreeNode):
            if not node:
                return -1
            else:
                left_p = _max_path(node.left)
                right_p = _max_path(node.right)
                if left_p + right_p + 2> self.ans:
                    self.ans = left_p + right_p + 2
                return max(left_p, right_p) + 1

        left_p = _max_path(root.left)
        right_p = _max_path(root.right)
        if left_p + right_p + 2 > self.ans:
            self.ans = left_p + right_p + 2
        return self.ans



