"""
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

输入:
11110
11010
11000
00000

输出: 1
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        并查集，find and join。先假设所有点独立，然后合并相邻的
        :return:
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        def find_root(tree: List[int], node: int) -> int:
            while tree[node] >=0:
                node = tree[node]
            return node


        # 用数组模拟树
        tree = [-1] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1':
                    tree[n*i+j] = n*i+j
                    continue

                root_cur = find_root(tree, i*n+j)
                next_i = i + 1
                next_j = j + 1
                # 下面的点
                if next_i < m:
                    if grid[next_i][j] == '1':
                        root_next = find_root(tree, next_i*n+j)
                        if root_cur != root_next:
                            num = tree[root_next]
                            tree[root_next] = root_cur
                            tree[root_cur] += num
                # 右边的点
                if next_j < n:
                    if grid[i][next_j] == '1':
                        root_next = find_root(tree, i*n+next_j)
                        if root_cur != root_next:
                            num = tree[root_next]
                            tree[root_next] = root_cur
                            tree[root_cur] += num
        print(tree)
        ans = 0
        for n in tree:
            if n < 0:
                ans += 1
        return ans


if __name__ == '__main__':
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    sol = Solution()
    print(sol.numIslands(grid))