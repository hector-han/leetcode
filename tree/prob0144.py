"""
二叉树的前序遍历 给定一个二叉树，返回它的 前序 遍历。
递归很简单，可以通过迭代完成吗

medium
1，递归,容易实现
2，自己想的迭代，使用栈，先左子树压栈，压栈后设置父节点为null,防止重复遍历，再右子树压栈。按压栈顺序访问，会破坏树结构
3，官网迭代，使用栈，先右子树压栈，再左子树压栈，按出栈顺序访问。好处是不破坏树结构。
4，3的空间复杂度是O(n),莫里斯遍历可以降到O(1)。其实所有节点访问了2次。思路是第一次访问时，在右子树的最后一个叶子，指向根。这样有个环可以找到根节点
   再次访问到跟节点就意味着右子树访问完毕。（第一次标志，right=null, 第二次标志，right=root)
"""

from utils import TreeNode, parse_tree
from typing import List




class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 迭代
        stack = []
        ans = []
        if root is None:
            return []
        stack.append(root)
        ans.append(root.val)

        while len(stack) > 0:
            node = stack[-1]
            if node.left is not None:
                stack.append(node.left)
                ans.append(node.left.val)
                node.left = None
            elif node.right is not None:
                stack.append(node.right)
                ans.append(node.right.val)
                node.right = None
            else:
                stack.pop()
        return ans


class Solution3:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = []
        ans = []
        stack.append(root)
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return ans


class Solution4:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
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
                    # 第一次遍历
                    ans.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    # 第二次遍历
                    predecessor.right = None
                    node = node.right
            else:
                ans.append(node.val)
                node = node.right
        return ans


if __name__ == '__main__':
    root = parse_tree([3,1,2])
    sol = Solution4()
    print(sol.preorderTraversal(root))
