"""
给定一个二叉树，返回它的中序 遍历。

medium

1、递归
2、
3、莫里斯遍历，第二次肯定要返回中心点，前序和中序都可以使用。

"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        ans = [root.val]
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + ans + right


class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans = []
        stack = []
        cur = root
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans


class Solution3:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans = []
        node = root
        while node:
            if node.left is not None:
                predecessor = node.left
                while True:
                    if predecessor.right is None or predecessor.right == node:
                        break
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = node
                    node = node.left
                else:
                    ans.append(node.val)
                    predecessor.right = None
                    node = node.right
            else:
                ans.append(node.val)
                node = node.right
                pass
        return ans


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3
    sol = Solution2()
    print(sol.inorderTraversal(n1))
