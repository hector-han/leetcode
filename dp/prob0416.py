"""
分割等和子集
medium
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        貌似是个0-1背包问题
        """
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2
        length = len(nums)
        # dp[i][j]前i个元素里，恰好有和=j的
        # dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        dp = [[False] * (target+1) for i in range(length+1)]
        for i in range(length+1):
            dp[i][0] = True
        for i in range(1, length+1):
            for j in range(target + 1):
                reminder = j - nums[i-1]
                if reminder >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][reminder]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[length][target]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 5, 11, 5]
    print(sol.canPartition(nums))
