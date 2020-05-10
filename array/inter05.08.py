"""
面试题 05.08. 绘制直线
绘制直线。有个单色屏幕存储在一个一维数组中，使得32个连续像素可以存放在一个 int 里。屏幕宽度为w，且w可被32整除（即一个 int 不会分布在两行上），屏幕高度可由数组长度及屏幕宽度推算得出。请实现一个函数，绘制从点(x1, y)到点(x2, y)的水平线。
给出数组的长度 length，宽度 w（以比特为单位）、直线开始位置 x1（比特为单位）、直线结束位置 x2（比特为单位）、直线所在行数 y。返回绘制过后的数组。

示例1:
 输入：length = 1, w = 32, x1 = 30, x2 = 31, y = 0
 输出：[3]
 说明：在第0行的第30位到第31为画一条直线，屏幕表示为[0b000000000000000000000000000000011]

"""
from typing import List

class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        binary_str = ['0'] * length * 32
        start_idx = y * w + x1
        end_idx = y * w + x2
        for i in range(start_idx, end_idx+1):
            binary_str[i] = '1'
        ans = []
        for i in range(length):
            s = i * 32
            e = i * 32 + 32
            b_rep = binary_str[s:e]
            num = int(''.join(b_rep), 2)
            if num >= 2 ** 31:
                num -= 2 ** 32
            ans.append(num)
        return ans

if __name__ == '__main__':
    length = 1
    w = 32
    x1 = 30
    x2 = 31
    y = 0
    sol = Solution()
    print(sol.drawLine(length, w, x1, x2, y))
