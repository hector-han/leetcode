"""
把二叉搜索树转换为累加树
easy
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13
"""
from utils import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        右，中，左的遍历，直接就可以
        """
        if not root:
            return root
        stack = []
        root_cache = root
        node = root
        last = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            node.val += last
            last = node.val
            node = node.left
        return root_cache


