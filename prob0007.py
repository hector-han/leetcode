"""
整数反转
easy

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

输入: 120
输出: 21

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

class Solution:
    def reverse(self, x: int) -> int:
        import math
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10

        n = len(digits)
        if n == 0:
            return 0
        start_idx = 0
        while digits[start_idx] == 0:
            start_idx += 1
        ans = 0
        for i in range(start_idx, n):
            ans = 10 * ans + digits[i]
        ans = ans * sign
        if ans < -math.pow(2, 31) or ans > math.pow(2, 31) - 1:
            return 0
        else:
            return ans


if __name__ == '__main__':
    x = 120
    sol = Solution()
    print(sol.reverse(x))
