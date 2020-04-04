"""
最长公共子序列
medium

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        if m == 0 or n == 0:
            return 0
        dp_table = []
        for i in range(m + 1):
            dp_table.append([0] * (n + 1))
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp_table[i+1][j+1] = dp_table[i][j] + 1
                else:
                    dp_table[i+1][j+1] = max(dp_table[i][j+1], dp_table[i+1][j])
        return dp_table[m][n]
