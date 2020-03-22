"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

medium

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

"""
from utils import TreeNode, parse_tree


class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, root: TreeNode) -> int:
        if root in self.memo:
            return self.memo[root]
        ans = 0
        if root is None:
            self.memo[root] = 0
            return 0
        if root.left is None:
            if root.right is None:
                ans = root.val
            else:
                ans =  max(self.rob(root.right), root.val + self.rob(root.right.left) + self.rob(root.right.right))
        else:
            if root.right is None:
                ans = max(self.rob(root.left), root.val + self.rob(root.left.left) + self.rob(root.left.right))
            else:
                tl = self.rob(root.left)
                tr = self.rob(root.right)
                grandchilds = [
                    self.rob(root.left.left),
                    self.rob(root.left.right),
                    self.rob(root.right.left),
                    self.rob(root.right.right)
                ]
                ans =  max(tl + tr, sum(grandchilds) + root.val)
        self.memo[root] = ans
        return ans


if __name__ == '__main__':
    tree_list = [3,2,3,None,3,None,1]
    tree = parse_tree(tree_list)
    sol = Solution()
    print(sol.rob(tree))
