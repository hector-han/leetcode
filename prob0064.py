"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        tmp = 0
        for i in range(m):
            tmp += grid[i][0]
            dp[i][0] = tmp
        tmp = 0
        for j in range(n):
            tmp += grid[0][j]
            dp[0][j] = tmp
        for i in range(1, m):
            for j in range(1, n):
                min_path = min(dp[i-1][j], dp[i][j-1])
                dp[i][j] = min_path + grid[i][j]
        return dp[m-1][n-1]