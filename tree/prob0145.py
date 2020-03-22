"""
二叉树的后续遍历

hard
1、递归
2、破坏树结构的,使用栈。先压跟节点，在牙右子树，再压左子树。压完设置为None防止重复访问
3、有点犯规的意思。 改变先序遍历 顺序为 根->右->左，那么逆序输出就是后续遍历
"""

from utils import TreeNode, parse_tree
from typing import List


class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [root]
        ans = []
        while stack:
            cur = stack[-1]
            if cur.left is None and cur.right is None:
                stack.pop()
                ans.append(cur.val)
                continue
            if cur.right is not None:
                stack.append(cur.right)
                cur.right = None
            if cur.left is not None:
                stack.append(cur.left)
                cur.left = None
        return ans


class Solution3:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return ans[::-1]


if __name__ == '__main__':
    i = [1, None, 2, None, None, 3, None]
    # i = [3,1,2]
    root = parse_tree(i)
    sol = Solution3()
    print(sol.postorderTraversal(root))