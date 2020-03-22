"""
easy
给定一个二叉树，检查它是否是镜像对称的。

1、两个参数递归
2、迭代，类似BFS，往队列中插入两个root, 一个先左后右，另一个先右后左。直到队列为空，或者中间不匹配。
"""


from utils import TreeNode
from utils import parse_tree

class Solution1:
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



class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        from collections import deque

        queue = deque([root, root])
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            if node1 is None:
                if node2 is None:
                    continue
                else:
                    return False
            else:
                if node2 is None:
                    return False
                else:
                    if node1.val != node2.val:
                        return False
                    queue.append(node1.left)
                    queue.append(node2.right)
                    queue.append(node1.right)
                    queue.append(node2.left)
        return True



if __name__ == '__main__':
    sol = Solution2()
    tree = [1,2,2,3,4,4,3]
    root = parse_tree(tree)
    print(sol.isSymmetric(root))

    tree = [1,2,2,None,3,None,3]
    root = parse_tree(tree)
    print(sol.isSymmetric(root))