"""
分割回文串 III
hard
给你一个由小写字母组成的字符串 s，和一个整数 k。

请你按下面的要求分割字符串：

首先，你可以将 s 中的部分字符修改为其他的小写英文字母。
接着，你需要把 s 分割成 k 个非空且不相交的子串，并且每个子串都是回文串。
请返回以这种方式分割字符串所需修改的最少字符数。

输入：s = "abc", k = 2
输出：1
解释：你可以把字符串分割成 "ab" 和 "c"，并修改 "ab" 中的 1 个字符，将它变成回文串。
1 <= k <= s.length <= 100
s 中只含有小写英文字母。
"""


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        # 保存(i, j) 需要替换多少次， j>i
        cache = {}
        for i in range(n):
            for j in range(i+1, n+1):
                ans = 0
                l, r = i, j - 1
                while l < r:
                    if s[l] != s[r]:
                        ans += 1
                    l += 1
                    r -= 1
                cache[(i, j)] = ans

        #dp[i][j]: 对于s的前i个字符，分割成j个子串的最小替换次数
        dp = [[0] * (k+1) for i in range(n+1)]
        for i in range(1, n+1):
            dp[i][1] = cache[(0, i)]

        for j in range(2, k+1):
            # 前j个分成j个，不用替换
            dp[j][j] = 0
            for i in range(j + 1, n+1):
                tmp = n
                for i0 in range(j-1, i):
                    tmp = min(tmp, dp[i0][j-1] + cache[(i0, i)])
                dp[i][j] = tmp
        return dp[n][k]


if __name__ == '__main__':
    sol = Solution()
    s = 'abc'
    k = 2
    print(sol.palindromePartition(s, k))