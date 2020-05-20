"""
路径总和 III
easy

给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

"""

from utils import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        prefixSum = {}
        prefixSum[0] = 1

        def recursive(node, prefixSum, target, current):
            """
            从root到当前节点，前缀和为current, 求target的路径个数
            """
            if not node:
                return 0
            res = 0
            current += node.val
            if current - target in prefixSum:
                res += prefixSum[current - target]
            if current not in prefixSum:
                prefixSum[current] = 0
            prefixSum[current] += 1
            res += recursive(node.left, prefixSum, target, current)
            res += recursive(node.right, prefixSum, target, current)
            prefixSum[current] -= 1
            return res

        return recursive(root, prefixSum, sum, 0)