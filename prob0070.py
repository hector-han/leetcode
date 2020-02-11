"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        动态规划，只要记录step-1和step-2的可能性即可
        :param n:
        :return:
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        num_last = 2
        num_second = 1
        for i in range(2, n):
            this_step = num_last + num_second
            num_second = num_last
            num_last = this_step
        return this_step


if __name__ == '__main__':
    sol = Solution()
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
