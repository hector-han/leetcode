"""
石子游戏
medium

亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false。

更一般化一下，题目要求结束时先手和后手谁的石子多，可以分别求结束时先手和后手石子的个数。

dp[i][j]: 是一个tuple, [i, j]这个区间内的石子情况。first,先手的个数；second,后手的个数。
初始化，dp[i][i][0] = piles[i], dp[i][i][1] = 0
迭代
求dp[i][j]，先手可以选择选左边还是选右边，故有两种可能
1、选左边
left = piles[i] + dp[i+1][j][1]
2、选右边
right = piles[j] + dp[i][j-1][1]
dp[i][j][0] = max(left, right)，dp[i][j][1]根据情况填写

"""
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = []
        for i in range(n):
            dp.append([ (0, 0) ] * n)
            dp[i][i] = (piles[i], 0)

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                print(i, j)
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    a = left
                    b = dp[i+1][j][0]
                else:
                    a = right
                    b = dp[i][j-1][0]
                dp[i][j] = (a, b)
        return dp[0][n-1][0] > dp[0][n-1][1]


if __name__ == '__main__':
    piles = [5,3,4,5]
    sol = Solution()
    print(sol.stoneGame(piles))

