"""
201 数字范围按位与
medium

给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

输入: [5,7]
输出: 4
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        从m到n, 如果位数不相当，直接=0，因为之后的各个位置都会取到0
        如果位数相当，那找最长的=1的前缀。11Xxxx->11Yyyy，X=0，Y=1，可以证明，后续位置，必然有0.
        所以只要找到最大的公共前缀1就可以。实现方式为右移动即可。
        """
        shift = 0
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift
