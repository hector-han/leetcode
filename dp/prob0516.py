"""
最长回文子序列
medium

bbbab -> 4 bbbb
cbbd -> 2 bb

dp[i][j] 位置i-j中的最长回文子序列
向两边扩展
if s[i-1] == s[j+1]
    dp[i-1][j+1] = dp[i][j] + 2
else
    dp[i-1][j+1] = max(dp[i-1][j], dp[i][j+1]

i: from n-1 to 0
j: from 0 to n-1
for all j<i, dp[i][j]=0
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length
        dp = []
        for i in range(length):
            dp.append([0] * length)
            dp[i][i] = 1
        for i in range(length-2, -1, -1):
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][length-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindromeSubseq('bbbab'))
    print(sol.longestPalindromeSubseq('cbbd'))
