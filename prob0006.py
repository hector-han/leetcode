"""
Z 字形变换

将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1:
            return s
        period = 2 * (numRows - 1)
        ans = ''
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                start = i
                while start < n:
                    ans += s[start]
                    start += period
            else:
                s1 = i
                s2 = period - s1
                while s2 < n:
                    ans += s[s1]
                    ans += s[s2]
                    s1 += period
                    s2 += period
                while s1 < n:
                    ans += s[s1]
                    s1 += period
        return ans


if __name__ == '__main__':
    s = "LEETCODEISHIRING"
    numRows = 4
    sol = Solution()
    print(sol.convert(s, numRows))


