"""
123. 买卖股票的最佳时机 III
hard

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][k][0]：第i天，能交易k次，不持有股票
        dp[i][k][1]：第i天，能交易k次，持有股票
        dp[i][k][0]=max(dp[i-1][k][0], dp[i-1][k][1]+p)
        dp[i][k][1]=max(dp[i-1][k][1], dp[i-1][k-1][0]-p)
        """
        dp_i_0 = [0] * 3 # var k
        dp_i_1 = [-float('inf')] * 3 # var k
        for p in prices:
            for k in range(1, 3):
                dp_i_0[k] = max(dp_i_0[k], dp_i_1[k] + p)
                dp_i_1[k] = max(dp_i_1[k], dp_i_0[k-1] - p)
        return dp_i_0[2]

if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    sol = Solution()
    ans = sol.maxProfit(prices)
    print(ans)
    assert ans == 6
