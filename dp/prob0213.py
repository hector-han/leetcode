"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
medium
房子组成一个环
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def rob_range(nums, s, e):
            dp_i_1 = 0
            dp_i_2 = 0
            dp_i = 0
            for i in range(e, s-1, -1):
                dp_i = max(nums[i] + dp_i_2, dp_i_1)
                dp_i_2 = dp_i_1
                dp_i_1 = dp_i
            return dp_i
        return max(rob_range(nums, 0, n-2), rob_range(nums, 1, n-1))


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    sol = Solution()
    print(sol.rob(nums))