"""
目标和
medium

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。

"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        递归, et
        """
        def recursive(i, j):
            if i == -1:
                if j == 0:
                    return 1
                else:
                    return 0
            return recursive(i-1, j-nums[i]) + recursive(i-1, j+nums[i])

        return recursive(len(nums)-1, S)


class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        动态规划，dp[i][j] 表示用数组中的前 i 个元素，组成和为 j 的方案数
        dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
        根据限制，下标可能为负数，
        """
        length = len(nums)
        dp = [[0] * 2001 for i in range(length)]
        dp[0][nums[0]+1000] += 1
        dp[0][-nums[0]+1000] += 1
        for i in range(1, length):
            for j in range(-1000, 1001):
                tmp = dp[i-1][j+1000]
                if tmp > 0:
                    dp[i][j+nums[i]+1000] += tmp
                    dp[i][j-nums[i]+1000] += tmp
        if S > 1000:
            return 0
        else:
            return dp[length-1][S+1000]




if __name__ == '__main__':
    sol = Solution()
    nums = [0,0,0,0,0,0,0,0,1]
    S = 1
    print(sol.findTargetSumWays(nums, S))