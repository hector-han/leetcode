"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        递归，或者动态规划
        """
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            ans = 0
            # 长度小于i的都已经计算完毕，现在计算长度为i的
            for j in range(i):
                num_left = j
                num_right = i-j-1
                # print(i, num_left, num_right)
                ans += (dp[num_left] * dp[num_right])
            dp[i] = ans
        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTrees(3))