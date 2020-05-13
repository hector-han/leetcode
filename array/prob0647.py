"""
回文子串
medium

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        枚举每个中心位置，向两边扩展，直到不能扩展。O(n^2)
        """
        n = len(s)
        if n == 1:
            return 1
        ans = 0
        # 中心位置是字
        for i in range(n):
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        # 中心位置为两个字符之间
        for i in range(n - 1):
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

if __name__ == '__main__':
    s = 'aabaaa'
    sol = Solution()
    # expect 12
    print(sol.countSubstrings(s))

