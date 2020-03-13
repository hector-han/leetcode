"""
根据一棵树的前序遍历与中序遍历构造二叉树。
"""
from utils import TreeNode
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        递归的计算，前序定位树根，在中序中找到树根，那么中序之前的就是左子树。在前序中数够个数，剩余的就是右子树
        :param preorder:
        :param inorder:
        :return:
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root_val = preorder[0]
        i = 0
        while i < len(inorder):
            if inorder[i] == root_val:
                break
            i += 1
        left_tree = self.buildTree(preorder[1: i+1], inorder[:i])
        right_tree = self.buildTree(preorder[i+1:], inorder[i+1:])
        root = TreeNode(root_val)
        root.left = left_tree
        root.right = right_tree
        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    sol = Solution()
    print('1')
    root = sol.buildTree(preorder, inorder)
    print('2')
    from tree import prob0094 as p94

    sol94 = p94.Solution()
    print(sol94.inorderTraversal(root))
