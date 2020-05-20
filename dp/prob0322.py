"""
零钱兑换
medium

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] 组成i面值的硬币，需要的最少硬币个数。 dp[i] = min(dp[i]-v for v in coins)
        max_coin = max(coins)
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for c in range(1, amount+1):
            cadidates = [dp[c - v] for v in coins if c-v >= 0 and dp[c-v] >= 0]
            if cadidates:
                dp[c] = min(cadidates) + 1

        return dp[amount]

if __name__ == '__main__':
    sol = Solution()
    coins = [2]
    amount = 11
    print(sol.coinChange(coins, amount))
