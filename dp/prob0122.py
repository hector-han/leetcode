"""
122. 买卖股票的最佳时机 II
easy

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0]: 第i天不持有股票
        dp[i][1]: 第i天持有股票
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - price[i])
        """
        dp_i_0 = 0
        dp_i_1 = -float('inf')

        for p in prices:
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + p)
            dp_i_1 = max(dp_i_1, tmp - p)
        return dp_i_0


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    sol = Solution()
    assert sol.maxProfit(prices) == 7
