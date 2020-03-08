"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
"""
from utils import TreeNode
from utils import parse_tree
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return [[]]

        queue = [root]
        ans = []
        finished = False
        while not finished:
            tmp = []
            queue2 = []
            finished = True
            for n in queue:
                tmp.append(n.val)
                if n.left is not None:
                    queue2.append(n.left)
                    finished = False
                if n.right is not None:
                    queue2.append(n.right)
                    finished = False
            ans.append(tmp)
            queue = queue2
        return ans


if __name__ == '__main__':
    sol = Solution()
    tree = [3,9,20,None,None,15,7]
    root = parse_tree(tree)
    print(sol.levelOrder(root))


