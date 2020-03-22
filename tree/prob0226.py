"""
翻转二叉树
easy

     4                     4
   /   \                 /   \
  2     7               7     2
 / \   / \             / \   / \
1   3 6   9          9   6 3   1
"""

from utils import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        left = root.left
        right = root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root


