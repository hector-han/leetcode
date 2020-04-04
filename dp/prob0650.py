"""
只有两个键的键盘
medium

最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：

Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
Paste (粘贴) : 你可以粘贴你上一次复制的字符。
给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。

回溯法
CV是一定要按的
最少按n次是可以的
CVXXXXX


从数学上可以证明，就是n的素数分解，然后把所有素因子加起来，不包括1

"""

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 2
        ans = []
        def back(i, num_screen, num_board, lastisC):
            if num_screen == n:
                ans.append(2+i)
                return
            elif num_screen > n:
                return
            else:
                if lastisC:
                    back(i+1, num_screen + num_board, num_board, False)
                else:
                    back(i+1, num_screen + num_board, num_board, False)
                    back(i+1, num_screen, num_screen, True)
        back(0, 2, 1, False)
        return min(ans)


class Solution2:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        res = 0

        d = 2
        while n > 1:
            while n % d == 0:
                res += d
                n = n // d
            d += 1
        return res


if __name__ == '__main__':
    sol = Solution2()
    print(sol.minSteps(4))

