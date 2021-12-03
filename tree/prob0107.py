"""
二叉树的层次遍历
easy
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回
[
  [15,7],
  [9,20],
  [3]
]
"""
from typing import List
from utils import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = []
        q.append(root)
        while q:
            num = len(q)
            tmp = []
            for i in range(num):
                ele = q.pop(0)
                tmp.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            ans.append(tmp)
        ans = ans[::-1]
        return ans

