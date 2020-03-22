"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i]为到0-i子序列的最高金额，则dp[i] = max(dp[i-2]+ nums[i], dp[i-1])
        dp[i-2]的很好理解，加了总比不加大；dp[i-1]的结尾如果在i-1取到，那一定不能有i；如果dp[i-1]在i-2取到，那么其实dp[i-2]必然
        在i-2取到，就退化到了第一种情况
        :return:
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]

        dp_last_last = 0
        dp_last = nums[0]
        ans = None
        for i in range(1, length):
            print(ans)
            ans = max(dp_last, dp_last_last + nums[i])
            dp_last_last = dp_last
            dp_last = ans
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([1,2,3,1]))
    print(sol.rob([2,7,9,3,1]))