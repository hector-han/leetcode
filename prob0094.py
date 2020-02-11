"""
给定一个二叉树，返回它的中序 遍历。
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # if root == None:
        #     return []
        # ans = [root.val]
        # left = self.inorderTraversal(root.left)
        # right = self.inorderTraversal(root.right)
        # return left + ans + right
        ans = []
        stack = []
        cur = root
        while cur != None or len(stack) > 0:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
        return ans

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3
    sol = Solution()
    print(sol.inorderTraversal(n1))
