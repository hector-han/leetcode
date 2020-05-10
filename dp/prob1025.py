"""
1025. 除数博弈
easy

爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。
只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。

"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        """
        先手是否能赢
        """
        dp = [False] * (N+1)
        for n in range(2, N+1):
            # 枚举所有因子
            for factor in range(1, n):
                if n % factor == 0:
                    if not dp[n-factor]:
                        dp[n] = True
                        break
        return dp[N]



