"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
medium

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        动态规划， dp[i][j] 以i,j为右下角的正方形的边长
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * n for i in range(m)]
        ans = 0
        for j in range(n):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                ans = max(ans, 1)
        for i in range(m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                ans = max(ans, 1)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    ans = max(ans, dp[i][j])
        return ans * ans



