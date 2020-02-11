"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：
    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        中序遍历之后是有序的
        """
        ret_list = []
        stack = []
        cur = root
        while cur != None or len(stack) > 0:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ret_list.append(cur.val)
                cur = cur.right
        print(ret_list)
        length = len(ret_list)
        if length <= 1:
            return True
        for i in range(length-1):
            if ret_list[i+1] <= ret_list[i]:
                return False
        return True


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(1)
    n1.left = n2

    sol = Solution()
    print(sol.isValidBST(n1))


