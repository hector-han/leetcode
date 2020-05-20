"""
汉明距离
easy

两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        r = x ^ y
        ans = 0
        while r > 0:
            ans += (r % 2)
            r = r // 2
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingDistance(1,4))