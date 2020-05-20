"""
完全平方数
medium

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        # 先找到<=n 的所有完全平方数
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i*i)
            i += 1

        dp = [0] * (n+1)
        for i in range(1, n+1):
            minimum = n
            for s in squares:
                if s > i:
                    break
                minimum = min(minimum, 1 + dp[i-s])
            dp[i] = minimum
        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))