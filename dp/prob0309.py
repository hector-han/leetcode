"""
最佳买卖股票时机含冷冻期
medium

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

dp[i][j]: 第i天是否持有股票，j=0,不持有；j=1,持有

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        times = len(prices)
        if times < 2:
            return 0
        dp = [[-float('inf')] * 2 for i in range(times + 1)]
        dp[0][0] = 0
        for i in range(times):
            # 今天不持有股票，可能是昨天不持有，也可能是卖掉了。含有冷冻期，买入时候，需要前两天
            # 这是因为，使用昨天不持有股票的收益，如果大于前天不持有，说明昨天卖出了。要排除。
            dp[i+1][0] = max(dp[i][0], dp[i][1] + prices[i])
            if i - 1 >= 0:
                dp[i+1][1] = max(dp[i-1][0] - prices[i], dp[i][1])
            else:
                dp[i+1][1] = max(dp[i][0] - prices[i], dp[i][1])
        return dp[times][0]



if __name__ == '__main__':
    prices = [1,2,3,0,2]
    sol = Solution()
    print(sol.maxProfit(prices))