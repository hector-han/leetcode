"""
从m*n矩阵的左上角到右下角共有多少种不同的路径
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # formula: choose (m-1) + (n-1) n-1
        # if (n-1) * (m-1) == 0:
        #     return 1
        # if m > n:
        #     a = m - 1
        #     b = n - 1
        # else:
        #     a = n - 1
        #     b = m - 1
        # # (a+b)!/a!/b!
        # def prod(start, end):
        #     ret = 1
        #     for i in range(end, start+1):
        #         ret *= i
        #     return ret
        # return prod(a+b, a+1) // prod(b, 1)
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
