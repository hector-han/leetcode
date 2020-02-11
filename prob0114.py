"""
给定一个二叉树，原地将它展开为链表。
"""
from utils import TreeNode
from utils import parse_tree

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        遇到右子树，先好缓存到栈中。把左子树接到右边。直到栈为空
        """
        if root is None:
            return 
        stack = []
        cur = root
        while True:
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is None:
                if len(stack) == 0:
                    return
                cur.right = stack.pop()
                cur = cur.right
            else:
                cur.right = cur.left
                cur.left = None
                cur = cur.right

if __name__ == '__main__':
    sol = Solution()
    tree = [1,2,5,3,4,None,6]
    root = parse_tree(tree)
    sol.flatten(root)

    cur = root
    while cur.right is not None:
        print(cur.val)
        cur = cur.right