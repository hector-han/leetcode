"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

medium

1、递归
2、使用队列

"""
from utils import TreeNode
from utils import parse_tree
from typing import List


class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)

            if node.left is not None:
                helper(node.left, level+1)
            if node.right is not None:
                helper(node.right, level+1)

        helper(root, 0)
        return levels


class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        from collections import deque
        levels = []
        level = 0
        queue = deque([root])
        while queue:
            levels.append([])
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return levels


if __name__ == '__main__':
    sol = Solution2()
    tree = [3,9,20,None,None,15,7]
    root = parse_tree(tree)
    print(sol.levelOrder(root))


