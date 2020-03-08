"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
"""
from utils import TreeNode
from utils import parse_tree


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)


if __name__ == '__main__':
    sol = Solution()
    tree = [3,9,20,None,None,15,7]
    root = parse_tree(tree)
    print(sol.maxDepth(root))
