"""
最长回文子串
medium

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

1、中心扩展法，从中心开始往两边扩展，直到最大长度
2、两个下标dp
3、Manacher算法，有点复杂
"""

class Solution1:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        ans = s[0]
        max_len = 1
        # 中心在字母上
        for i in range(n):
            offset = 1
            while i-offset >= 0 and i+offset<n:
                if s[i-offset] == s[i+offset]:
                    if 2*offset+1 > max_len:
                        ans = s[i-offset:i+offset+1]
                        max_len = 2*offset+1
                else:
                    break
                offset += 1

        # 中心在字母中间
        for i in range(n-1):
            offset = 0
            left = i - offset
            right = i + 1 + offset

            while left >= 0 and right < n:
                if s[left] == s[right]:
                    if 2*offset+2>max_len:
                        ans = s[left:right+1]
                        max_len = 2*offset+2
                else:
                    break
                offset += 1
                left = i - offset
                right = i + 1 + offset

        return ans


if __name__ == '__main__':
    s='cbbd'
    sol = Solution1()
    print(sol.longestPalindrome(s))
