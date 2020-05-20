"""
二叉树的最近公共祖先
medium


给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
"""
from utils import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        定义 f(x)为x节点的子树中保护p或q中的一个
        那么最近公共祖先x, x的左子树l, 右子树r,满足
        (f(l) && f(r))
        || ((x==p || x==q) && (f(l) || f(r)))
        """
        self.ans = None
        def dfs(root: TreeNode, p: TreeNode, q: TreeNode):
            if not root:
                return False
            lson = dfs(root.left, p, q)
            rson = dfs(root.right, p, q)
            if (lson and rson) or ((root == p or root == q) and (lson or rson)):
                self.ans = root
            return lson or rson or (root == p) or (root == q)

        dfs(root, p, q)
        return self.ans