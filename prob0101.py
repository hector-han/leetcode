"""
给定一个二叉树，检查它是否是镜像对称的。
"""


from utils import TreeNode
from utils import parse_tree

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recursiveMath(n1, n2):
            if n1 is None:
                if n2 is None:
                    return True
                else:
                    return False
            else:
                if n2 is None:
                    return False
            if n1.val != n2.val:
                return False
            r1 = recursiveMath(n1.left, n2.right)
            if not r1:
                return False
            r2 = recursiveMath(n1.right, n2.left)
            return r2

        return recursiveMath(root, root)


if __name__ == '__main__':
    sol = Solution()
    tree = [1,2,2,3,4,4,3]
    root = parse_tree(tree)
    print(sol.isSymmetric(root))

    tree = [1,2,2,None,3,None,3]
    root = parse_tree(tree)
    print(sol.isSymmetric(root))